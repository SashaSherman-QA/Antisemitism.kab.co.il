from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WindowsHandler:
    def __init__(self, driver):
        self.driver = driver

    def get_main_window_handle(self):
        return self.driver.current_window_handle

    def open_main_window(self, url):
        self.driver.get(url)
        return self.driver.current_window_handle

    def click_link_and_open_new_window(self, link_locator, expected_url):
        main_window_handle = self.driver.current_window_handle

        # Click the link that opens a new window
        link = self.driver.find_element(*link_locator)
        link.click()

        # Wait for the new window to open
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        # Switch to the new window
        new_window_handle = WindowsHandler.switch_to_new_window(self.driver, main_window_handle)

        # Verify the URL of the new window and close it
        WindowsHandler.verify_and_close_new_window(self.driver, expected_url)

        return new_window_handle

    @staticmethod
    def switch_to_new_window(driver, main_window_handle):
        all_handles = driver.window_handles
        new_window_handle = [handle for handle in all_handles if handle != main_window_handle][0]
        driver.switch_to.window(new_window_handle)
        return new_window_handle

    @staticmethod
    def verify_and_close_new_window(driver, expected_url):
        actual_url = driver.current_url

        if expected_url in actual_url:
            print("New window opened with the expected URL.")
        else:
            print(f"New window opened with a different URL: {actual_url}")

        driver.close()