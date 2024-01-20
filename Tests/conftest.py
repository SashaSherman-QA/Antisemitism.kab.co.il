import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from Tests.Utilities.Urls import Urls
from Tests.Utilities.BaseClass import BaseClass


# @pytest.fixture(scope="class")
@pytest.fixture
# def get_driver(request):  # for use with scope=class, request.cls.driver, etc...
def get_driver():
        chrome_options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)  # keeps browser open in end of run (if driver.quit is commented)
        chrome_options.add_argument("--headless")  # Add this line to enable headless mode
        chrome_options.add_argument("--window-size=1920x1080")  # in case of headless mode
        _driver = webdriver.Chrome(options=chrome_options)
        # _driver.maximize_window()  # in case of non-headless mode, when browser window is opened
        # _driver.set_window_size(1500, 1214)  # didn't work without headless mode
        _driver.get(Urls.home_page_url)
        # WebDriverWait(_driver, 20).until(lambda driver: driver.execute_script(
        #                                      "return window.performance.timing.loadEventEnd > 0"))
        # _driver.implicitly_wait(10)
        page_width = _driver.execute_script("return window.innerWidth")
        BaseClass.page_width = page_width
        BaseClass.log_info(f"page_width_from_conftest = {page_width}")
        yield _driver
        _driver.quit()


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in the HTML report whenever a test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.get_plugin('html')
#
#     if pytest_html is not None:
#         outcome = yield
#         report = outcome.get_result()
#         extra = getattr(report, 'extra', [])
#
#         if report.when == 'call' or report.when == "setup":
#             xfail = hasattr(report, 'wasxfail')
#             if (report.skipped and xfail) or (report.failed and not xfail):
#                 driver = item.funcargs.get('get_driver')  # Obtain the instance-level driver
#                 if driver:
#                     file_name = report.nodeid.replace("::", "_") + ".png"
#                     _capture_screenshot(driver, file_name)
#                     if file_name:
#                         html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                                'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                         extra.append(pytest_html.extras.html(html))
#                 report.extra = extra


# def _capture_screenshot(driver, name):
#     driver.get_screenshot_as_file(name)




