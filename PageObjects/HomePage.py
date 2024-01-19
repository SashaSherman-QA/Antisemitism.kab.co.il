from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from Tests.Utilities.BaseClass import BaseClass
import requests


class HomePage():

    # Locator - monthly donation popup
    donation_popup = (By.CSS_SELECTOR, 'a[href="#close"]')

    # Locators - Section 0
    section0_text1 = (By.XPATH, r"//div[contains(@class, 'et_pb_section_0')]//p[contains(text(),'אנטישמיות הסיפור האמיתי!')]")
    section0_text2 = (By.XPATH, r"//div[contains(@class, 'et_pb_section_2')]//span[contains(text(),'איך ייתכן שבשנת 2023')]")
    section0_text3 = (By.XPATH, r"//div[contains(@class, 'et_pb_section_2')]//span[contains(text(),'הפתרון לשנאת ישראל')]")
    section0_link = (By.XPATH, r"//div[contains(@class, 'et_pb_section_2')]//a[1]")

    # Locators - Section 4
    section4_links = (By.XPATH, r"//article[contains( @class, 'et_pb_post')]//a") # posts 1-9 , post#0 is not from section4 (exclude)
    all_links = (By.XPATH, r"//a")

    # Locators - Section 10
    video_lama_sonim = (By.CSS_SELECTOR, 'iframe[title*="למה שונאים יהודים"]')

    @staticmethod
    def check_section_0_elements(driver):
        assert BaseClass.wait_and_get_element(driver, *HomePage.section0_text1).is_displayed(), "section 0 - text1 missing"
        assert BaseClass.wait_and_get_element(driver, *HomePage.section0_text2).is_displayed(), "section 0 - text2 missing"
        assert BaseClass.wait_and_get_element(driver, *HomePage.section0_text3).is_displayed(), "section 0 - text3 missing"

    @staticmethod
    def treat_donation_popup(driver):
        if BaseClass.is_element_visible(driver, *HomePage.donation_popup):
            BaseClass.click_button(driver, *HomePage.donation_popup)

    @staticmethod
    def check_section4_links(driver):
        section4_links = BaseClass.get_href_attributes(driver, *HomePage.section4_links)
        unique_links_section4 = list(set(section4_links))
        print("\nall links:", len(unique_links_section4), "unique links:", len(section4_links))
        unique_http_links_section4 = [link for link in unique_links_section4 if "http" in link]

        for link_url in unique_links_section4:
            try:
                response = requests.get(link_url)
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
                print(f"Link {link_url} is accessible. Status code: {response.status_code}")
            except requests.RequestException as e:
                print(f"Link {link_url} is not accessible. Error: {e}")

    @staticmethod
    def check_all_links(driver):
        all_links_on_page = BaseClass.get_href_attributes(driver, *HomePage.all_links)
        all_unique_links = list(set(all_links_on_page))
        all_unique_http_links = [link for link in all_unique_links if "http" in link]
        # print("\nall http links:", len(all_links_on_page), ", all unique http links:", len(all_unique_http_links))
        BaseClass.log_info(f"All http links: {len(all_links_on_page)}, all unique http links:, {len(all_unique_http_links)}")
        errors = []
        for link_url in all_unique_http_links:
            response = requests.get(link_url, allow_redirects=True)
            # response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            # assert response.status_code // 100 == 2, f"Unexpected status code: {response.status_code}"
            if response.status_code // 100 == 2:
                # print(f"Link {link_url} is accessible. Status code: {response.status_code}")
                BaseClass.log_info(f"Link {link_url} is accessible. Status code: {response.status_code}")
            elif response.status_code == 302:  # Status code for a redirect
                # Access the 'Location' header to get the redirected URL
                redirected_url = response.headers['Location']
                # print(f"Redirected to: {redirected_url}")
                BaseClass.log_warning(f"Redirected to: {redirected_url}")
                redirected_response = requests.get(redirected_url)
                if redirected_response.status_code // 100 == 2:
                    # print(f"Redirected link {link_url} is accessible. Status code: {redirected_response.status_code}")
                    BaseClass.log_warning(f"Redirected link {link_url} is accessible. Status code: {redirected_response.status_code}")
            else:
                if "twitter" not in link_url:  # requests.get returns 400 , but manual test passes after redirect
                    BaseClass.log_error(f"Link {link_url} is NOT accessible. Status code: {response.status_code}")
                    errors.append(f"Error: {link_url}")

        if errors:
            raise AssertionError("\n".join(errors))
