
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.HomePage import HomePage
from PageObjects.Header import Header
from Tests.Utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
class TestLink(BaseClass):
    def test_link(self, get_driver):
        driver = get_driver
        home_page = HomePage(driver)
        link = driver.find_element(*home_page.section0_link_locator);
        link.click()