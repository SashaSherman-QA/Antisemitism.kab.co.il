import inspect
import logging
from Tests.Utilities.Urls import Urls
from Tests.Utilities.Translate2Eng import transliterate_hebrew_to_latin
# from unidecode import unidecode
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from Tests.Utilities.LoggerModule import setup_logger


class BaseClass:
    logger = setup_logger()

    @staticmethod
    def log_info(message):
        BaseClass.logger.info(message)

    @staticmethod
    def log_warning(message):
        BaseClass.logger.warning(message)

    @staticmethod
    def log_error(message):
        BaseClass.logger.error(message)
    # @classmethod
    # def get_logger(cls):  # you can use BaseClass.logger instead cls, then no need to pass cls as input parameter
    #     if cls.logger is None:
    #         logger_name = inspect.stack()[1][3]  # using a trick to solve the name problem
    #         cls.logger = logging.getLogger(logger_name)
    #         # logger = logging.getLogger(__name__)  # will give BaseClass name instead the calling test method name
    #         file_handler = logging.FileHandler('logfile.log')
    #         cls.logger.addHandler(file_handler)  # pass file handler
    #         formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    #         file_handler.setFormatter(formatter)
    #         cls.logger.setLevel(logging.INFO)  # info and above(error, critical)
    #     return cls.logger

    @staticmethod
    def select_option_by_text(element, text):  # In static method, self is not used, as in instance methods
        dropdown = Select(element)
        dropdown.select_by_visible_text(text)
        # Static DropDown - use Select class (when element has select tag), pass element as parameter, use its methods.
        # dropdown.select_by_index(1)  # another option to select Female

    @staticmethod
    def is_element_visible(driver, by, value, timeout=10):
        try:
            element = BaseClass.wait_and_get_element(driver, by, value, timeout)
            return element.is_displayed()
        except Exception:
            return False

    @staticmethod
    def wait_for_element_to_be_clickable(driver, by, value, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    @staticmethod
    def is_element_clickable(driver, by, value, timeout=10):
        try:
            element = BaseClass.wait_for_element_to_be_clickable(driver, by, value, timeout)
            return True
        except Exception:
            return False

    @staticmethod
    def wait_and_get_element(driver, by, value, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    @staticmethod
    def wait_and_get_elements(driver, by, value, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located((by, value))
        )

    @staticmethod
    def wait_and_get_elements_if_present(driver, by, value, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )

    @staticmethod
    def get_href_attributes(driver, by, value, timeout=10):
        elements = BaseClass.wait_and_get_elements_if_present(driver, by, value, timeout)
        return [element.get_attribute("href") for element in elements]

    @staticmethod
    def click_link_and_assert_url(driver, by, value, exp_url):
        link = driver.find_element(by, value);
        link.click()
        WebDriverWait(driver, 5).until(EC.url_to_be(exp_url))
        assert driver.current_url == exp_url

    @staticmethod
    def click_button(driver, by, value):
        button = BaseClass.wait_and_get_element(driver, by, value)
        isClickable = BaseClass.is_element_clickable(driver, by, value)
        if isClickable:
            button.click()

    @staticmethod
    def is_element_visible(driver, by, value, timeout=10):
        try:
            element = BaseClass.wait_and_get_element(driver, by, value, timeout)
            return element.is_displayed()
        except Exception:
            return False

    @staticmethod
    def check_video(driver, by, value, width_ratio, height_width_ratio):
        log = BaseClass.get_logger()
        iframe_element = BaseClass.wait_and_get_element(driver, by, value)
        video_title = iframe_element.get_attribute('title')
        driver.switch_to.frame(iframe_element)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body')))
        video = BaseClass.wait_and_get_element(driver, By.CSS_SELECTOR, 'video[class="video-stream html5-main-video"]')
        style_attribute = video.get_attribute('style')

        width_start = style_attribute.find('width:') + len('width:')
        width_end = style_attribute.find('px', width_start)
        video_width = int(style_attribute[width_start:width_end])

        height_start = style_attribute.find('height:') + len('height:')
        height_end = style_attribute.find('px', height_start)
        video_height = int(style_attribute[height_start:height_end])

        page_width = driver.execute_script("return window.innerWidth")
        percentage_of_page_width = (video_width / page_width) * 100
        percentage_of_height_width = (video_height/video_width) * 100
        transliterated_title = transliterate_hebrew_to_latin(video_title)
        log.info(f"video_title: {transliterated_title}")
        # log.info(f"video_title: {video_title}")
        log.info(f"video_width = {video_width}")
        log.info(f"video_height = {video_height}")
        log.info(f"(video_width / page_width) * 100 = {percentage_of_page_width}")
        log.info(f"(video_width / video_height) * 100 = {percentage_of_height_width}")

        assert percentage_of_page_width == width_ratio, "video dimensions are incorrect"
        assert percentage_of_height_width > height_width_ratio, "video dimensions are incorrect"
        # assert  40 <= percentage_of_page_width <=60, "video dimensions are incorrect"
        # return to main frame
        driver.switch_to.default_content()

    @staticmethod
    def back_and_check(driver):
        try:
            driver.back()
            WebDriverWait(driver, 10).until(EC.url_to_be(Urls.home_page_url))
            assert driver.current_url == Urls.home_page_url
        except TimeoutException:
            print("Timed out waiting for the URL to be", Urls.home_page_url)
        except Exception as e:
            print(f"An error occurred in back action: {e}")