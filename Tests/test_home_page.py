from PageObjects.HomePage import HomePage
from PageObjects.Header import Header
from Tests.Utilities.BaseClass import BaseClass
from Tests.Utilities.Urls import Urls


# py.test .\test_home_page.py --html=Antisemitism_Report.html

class TestHomePage(BaseClass):
    def test_home_page(self, get_driver):
        driver = get_driver
        BaseClass.treat_donation_popup(driver)  # If exists - close
        Header.check_header(driver) # that all menu items displayed
        BaseClass.check_text_elements_displayed_single_locator(
            driver, HomePage.section0_text_elements_locator, HomePage.section0_strings_from_text)
        BaseClass.check_images_single_locator(driver, HomePage.section8_images_single_locator, 20, 50)
        BaseClass.check_video_in_iframe(driver, HomePage.section10_iframe_video_lama_sonim_locator, 40, 50)
        BaseClass.check_all_links(driver)

        # Example:
        # BaseClass.check_text_elements_displayed_locators_list(
        #     driver, HomePage.section0_text_elements_locators, HomePage.section0_strings_from_text)


