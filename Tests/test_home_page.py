from PageObjects.HomePage import HomePage
from PageObjects.Header import Header
from Tests.Utilities.BaseClass import BaseClass
from Tests.Utilities.Urls import Urls


# py.test .\test_home_page.py --html=Antisemitism_Report.html

class TestHomePage(BaseClass):
    def test_home_page(self, get_driver):
        driver = get_driver
        # HomePage.treat_donation_popup(driver)  # If exists - close
        # Header.check_header(driver) # that all menu items displayed
        # HomePage.check_section_0_elements(driver)
        # BaseClass.check_video(driver, *HomePage.video_lama_sonim, 100, 49)
        # BaseClass.click_link_and_assert_url(driver, *HomePage.section0_link, Urls.odot_url)
        # BaseClass.back_and_check(driver)
        # HomePage.check_section4_links(driver)
        HomePage.check_all_links(driver)



