from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_pages import BasePage


class LoginPage(BasePage):

    def __init__(self):
        super().__init__(self)
        self.username_input = (By.XPATH, "//*[contains(@resource-id,'Username')]")
        self.username_input_appium = (AppiumBy.ACCESSIBILITY_ID, "")
        self.password_input = (By.XPATH, "//*[contains(@resource-id,'Password')]")
        self.login_button = (By.CLASS_NAME, "android.widget.Button")
        self.skip_button = (By.XPATH, "//*[contains(@text,'Überspringen')]")
        self.bottom_navigation = (By.XPATH, "//*[contains(@text,'')]")

    def login(self, username, password) -> None:
        self.find_element_and_send_key(self.username_input, username)
        self.find_element_and_send_key(self.password_input, password)
        self.find_element_and_click(self.login_button)
        self.find_element_and_click(self.skip_button)
        self.find_element_and_click(self.skip_button)
        self.find_element_and_click(self.skip_button)

    def isUserSignedIn(self) -> bool:
        return self.is_element_enabled(self.bottom_navigation)



