import pytest
from selenium import webdriver
from Tests.Utilities.Urls import Urls


# @pytest.fixture(scope="class")
@pytest.fixture
# def get_driver(request):  # for use with scope=class, request.cls.driver, etc...
def get_driver(request):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # keeps browser open in end of run (if driver.quit is commented)
        _driver = webdriver.Chrome(options=options)
        _driver.get(Urls.home_page_url)
        _driver.maximize_window()
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




