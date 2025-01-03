from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_pages import BasePage


class ProfilePage(BasePage):

    def __init__(self):
        super().__init__(self)
        self.device = (By.XPATH, "//*[contains(@resource-id,'Username')]")
        self.user_icon = (AppiumBy.ACCESSIBILITY_ID, "")
        self.device_counter = (By.XPATH, "//*[contains(@resource-id,'Password')]")
        self.spinner = (By.CLASS_NAME, "android.widget.ProgressBar")

    def wait_until_spinner_will_be_invisible(self):
        el = self.find_all_elements(self.spinner)
        if el:
            self.wait_until_element_will_be_invisible(el[0])

    def proceed_to_profile_page(self) -> None:
        self.find_element_and_click(self.device)
        self.find_element_and_click(self.user_icon)

    def validateDeviceCounter(self, counter) -> bool:
        return self.is_element_equal(self.device_counter, counter)



