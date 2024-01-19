from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage


class OdotPage(BasePage):

    # Locators - Section 0
    section0_text1 = (By.XPATH, r"//div[contains(@class, 'et_pb_section_0')]//p[contains(text(),'אנטישמיות הסיפור האמיתי!')]")

    # ==== Section 0 ====
    def get_section0_text1(self):
        return self.wait_and_get_element(*OdotPage.section0_text1)

