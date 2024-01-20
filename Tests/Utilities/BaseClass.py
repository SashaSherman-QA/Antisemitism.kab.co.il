import requests
from Tests.Utilities.Urls import Urls
from Tests.Utilities.Translate2Eng import transliterate_hebrew_to_latin
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from Tests.Utilities.LoggerModule import setup_logger
from Tests.Utilities.Translate2Eng import transliterate_hebrew_to_latin_mapping


class BaseClass:
    logger = setup_logger()
    donation_popup = (By.CSS_SELECTOR, 'a[href="#close"]') # Locator - monthly donation popup
    page_width = 1

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
    def is_element_visible(driver, locator, timeout=10):
        try:
            element = BaseClass.wait_and_get_element(driver, locator, timeout)
            return element.is_displayed()
        except Exception:
            return False

    @staticmethod
    def wait_for_element_to_be_clickable(driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def is_element_clickable(driver, locator, timeout=10):
        try:
            element = BaseClass.wait_for_element_to_be_clickable(driver, locator, timeout)
            return True
        except Exception:
            return False

    @staticmethod
    def wait_and_get_element(driver, locator, timeout=20):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )


    @staticmethod
    def wait_and_get_elements(driver, elements_locator, timeout=30):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located(elements_locator)
        )

    @staticmethod
    def wait_and_get_elements_if_present(driver, locator, timeout=20):
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @staticmethod
    def get_href_attributes(driver, locator):
        elements = BaseClass.wait_and_get_elements_if_present(driver,locator)
        return [element.get_attribute("href") for element in elements]

    @staticmethod
    def click_link_and_assert_url(driver, by, value, exp_url):
        link = driver.find_element(by, value);
        link.click()
        WebDriverWait(driver, 5).until(EC.url_to_be(exp_url))
        assert driver.current_url == exp_url

    @staticmethod
    def click_button(driver, locator):
        button = BaseClass.wait_and_get_element(driver, locator)
        is_clickable = BaseClass.is_element_clickable(driver, locator)
        if is_clickable:
            button.click()

    @staticmethod
    def is_element_visible(driver, locator):
        try:
            element = BaseClass.wait_and_get_element(driver, locator)
            return element.is_displayed()
        except Exception:
            return False

    @staticmethod
    def check_video_in_iframe(driver, locator, width_ratio, height_width_ratio):
        iframe_element = BaseClass.wait_and_get_element(driver, locator)
        video_title = iframe_element.get_attribute('title')
        driver.switch_to.frame(iframe_element)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body')))
        video_locator_inside_iframe = (By.CSS_SELECTOR, 'video[class="video-stream html5-main-video"]')
        video = BaseClass.wait_and_get_element(driver, video_locator_inside_iframe)
        style_attribute = video.get_attribute('style')

        width_start = style_attribute.find('width:') + len('width:')
        width_end = style_attribute.find('px', width_start)
        video_width = int(style_attribute[width_start:width_end])

        height_start = style_attribute.find('height:') + len('height:')
        height_end = style_attribute.find('px', height_start)
        video_height = int(style_attribute[height_start:height_end])

        # page_width = driver.execute_script("return window.innerWidth")
        page_width = BaseClass.page_width

        percentage_of_page_width = (video_width / BaseClass.page_width) * 100
        percentage_of_height_width = (video_height/video_width) * 100
        # transliterated_title = transliterate_hebrew_to_latin(video_title)
        transliterated_title = transliterate_hebrew_to_latin_mapping(video_title)
        BaseClass.log_info(f"video_title: {transliterated_title}")
        # BaseClass.log_info(f"video_title: {video_title}")

        BaseClass.log_info(f"video_width = {video_width}")
        BaseClass.log_info(f"page_width = {BaseClass.page_width}")
        BaseClass.log_info(f"video_height = {video_height}")
        BaseClass.log_info(f"(video_width / page_width) * 100 = {percentage_of_page_width}")
        BaseClass.log_info(f"(video_width / video_height) * 100 = {percentage_of_height_width}")
        assert percentage_of_page_width > width_ratio, "video width dimensions are incorrect"
        assert percentage_of_height_width > height_width_ratio, "video height dimensions are incorrect"
        # assert  40 <= percentage_of_page_width <=60, "video dimensions are incorrect"

        driver.switch_to.default_content() # return to main frame

    @staticmethod
    def check_images_single_locator(driver, elements_locator, width_ratio, height_width_ratio):
        # elements = BaseClass.wait_and_get_elements(driver, elements_locator)
        elements = BaseClass.wait_and_get_elements_if_present(driver, elements_locator)

        for index, element in enumerate(elements):
            BaseClass.check_image(driver, element, width_ratio, height_width_ratio)

    @staticmethod
    def check_images_locators_list(driver, elements_locators, width_ratio, height_width_ratio):
        for element_locator in elements_locators:
            element = BaseClass.wait_and_get_element(driver, element_locator)
            BaseClass.check_image(driver, element, width_ratio, height_width_ratio)

    @staticmethod
    def check_image(driver, element, width_ratio, height_width_ratio):
        width_str = driver.execute_script(
            "return window.getComputedStyle(arguments[0], null).getPropertyValue('width');",element)
        height_str = driver.execute_script(
            "return window.getComputedStyle(arguments[0], null).getPropertyValue('height');",element)
        width = int(float(width_str.rstrip("px")))
        height = int(float(height_str.rstrip("px")))
        percentage_of_page_width = (width / BaseClass.page_width) * 100
        percentage_of_height_width = (height / width) * 100
        image_source = element.get_attribute("src")
        BaseClass.log_info(f"image_src = {image_source}")
        BaseClass.log_info(f"image_width = {width}")
        BaseClass.log_info(f"page_width = {BaseClass.page_width}")
        BaseClass.log_info(f"image_height = {height}")
        BaseClass.log_info(f"(Image: width / page_width) * 100 = {percentage_of_page_width}, Expected: {width_ratio}")
        BaseClass.log_info(f"(Image: width / height) * 100 = {percentage_of_height_width}, Expected: {height_width_ratio}")
        assert percentage_of_page_width > width_ratio, "image width dimensions are incorrect"
        assert percentage_of_height_width > height_width_ratio, "image height dimensions are incorrect"
        # assert  40 <= percentage_of_page_width <=60, "video dimensions are incorrect"

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

    @staticmethod
    def check_all_links(driver):
        all_links_locator = (By.XPATH, r"//a")
        all_links_on_page = BaseClass.get_href_attributes(driver, all_links_locator)
        all_unique_links = list(set(all_links_on_page))
        all_unique_http_links = [link for link in all_unique_links if "http" in link]
        # print("\nall http links:", len(all_links_on_page), ", all unique http links:", len(all_unique_http_links))
        BaseClass.log_info(f"All http links: {len(all_links_on_page)}, all unique http links:, {len(all_unique_http_links)}")
        errors = []
        for link_url in all_unique_http_links:
            response = requests.get(link_url, allow_redirects=True)
            # response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            if response.status_code // 100 == 2:
                BaseClass.log_info(f"Link {link_url} is accessible. Status code: {response.status_code}")
            elif response.status_code == 302:  # Status code for a redirect
                redirected_url = response.headers['Location']  # redirected URL
                BaseClass.log_warning(f"Redirected to: {redirected_url}")
                redirected_response = requests.get(redirected_url)
                if redirected_response.status_code // 100 == 2:
                    BaseClass.log_warning(f"Redirected link {link_url} is accessible. Status code: {redirected_response.status_code}")
            else:
                if "twitter" not in link_url:  # requests.get returns 400 , but manual test passes after redirect
                    BaseClass.log_error(f"Link {link_url} is NOT accessible. Status code: {response.status_code}")
                    errors.append(f"Error: {link_url}")
        if errors:
            raise AssertionError("\n".join(errors))

    @staticmethod
    def check_text_elements_displayed_locators_list(driver, locators_list, strings_from_text):
        for index, locator in enumerate(locators_list):
            english_string = transliterate_hebrew_to_latin_mapping(strings_from_text[index])
            assert BaseClass.wait_and_get_element(driver, locator).is_displayed(), \
                f"Element with text including the string not displayed. Translit String: {english_string}"
            BaseClass.log_info(f"Locators List: Element with following locator was displayed properly:  {english_string}")

    # @staticmethod
    # def check_images_single_locator(driver, elements_locator, width_ratio, height_width_ratio):
    #     # elements = BaseClass.wait_and_get_elements(driver, elements_locator)
    #     elements = BaseClass.wait_and_get_elements_if_present(driver, elements_locator)


    @staticmethod
    def check_text_elements_displayed_single_locator(driver, elements_locator, strings_from_text):
        text_elements = BaseClass.wait_and_get_elements_if_present(driver, elements_locator)
        for index, element in enumerate(text_elements):
            english_string = transliterate_hebrew_to_latin_mapping(strings_from_text[index])
            assert element.is_displayed(), \
                f"Element with text including the string not displayed. Translit String: {english_string}"
            BaseClass.log_info(f"Single Locator: Element with following locator was displayed properly:  {english_string}")

    @staticmethod
    def treat_donation_popup(driver):
        if BaseClass.is_element_visible(driver, BaseClass.donation_popup):
            BaseClass.click_button(driver, BaseClass.donation_popup)
