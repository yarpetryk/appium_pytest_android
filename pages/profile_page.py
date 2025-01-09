import time

from selenium.webdriver.common.by import By
from pages.base_pages import BasePage


class ProfilePage(BasePage):

    device = (By.XPATH, "//*[contains(@text,'prosumer')]")
    user_icon = (By.XPATH, "//*[contains(@resource-id,'ll_top_icons')]/child::*[position()=2]")
    device_counter = (By.XPATH, "//*[contains(@text,'Devices')]/following-sibling::*[position()=1]")
    spinner = (By.CLASS_NAME, "android.widget.ProgressBar")

    def wait_until_spinner_will_be_invisible(self):
        el = self.find_all_elements(self.spinner)
        if el:
            self.wait_until_element_will_be_invisible(el[0])

    def proceed_to_profile_page(self) -> None:
        self.find_element_and_click(self.device)
        time.sleep(2)
        self.find_element_and_click(self.user_icon)

    def validate_device_counter(self, counter) -> bool:
        return self.is_element_equal(self.device_counter, str(counter))





