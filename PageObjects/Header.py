from selenium.webdriver.common.by import By
from Tests.Utilities.BaseClass import BaseClass


class Header():
    # Locators - Top Menu
    logo = (By.ID, "logo")
    odot = (By.XPATH, r"//ul[@id='top-menu']//a[text()='אודות']")
    maamarim = (By.XPATH, r"//ul[@id='top-menu']//a[text()='מאמרים']")
    projectim = (By.XPATH, r"//ul[@id='top-menu']//a[text()='פרויקטים']")
    mekorot = (By.XPATH, r"//ul[@id='top-menu']//a[text()='מקורות']")
    sheelot_ve_tshuvot = (By.XPATH, r"//ul[@id='top-menu']//a[text()='שאלות ותשובות']")

    @staticmethod
    def check_header(driver):
        assert BaseClass.wait_and_get_element(driver, Header.logo).is_displayed(), "logo is missing"
        assert BaseClass.wait_and_get_element(driver, Header.odot).is_displayed(), "odot is missing"
        assert BaseClass.wait_and_get_element(driver, Header.maamarim).is_displayed(), "maamarim is missing"
        assert BaseClass.wait_and_get_element(driver, Header.mekorot).is_displayed(), "mekorot is missing"
        assert BaseClass.wait_and_get_element(driver, Header.projectim).is_displayed(), "projectim is missing"
        assert BaseClass.wait_and_get_element(driver, Header.sheelot_ve_tshuvot).is_displayed(), "sheelot ve tshuvot is missing"