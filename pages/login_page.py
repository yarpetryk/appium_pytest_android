from selenium.webdriver.common.by import By
from pages.base_pages import BasePage


class LoginPage(BasePage):

    login_button_welcome = (By.XPATH, "//*[contains(@resource-id,'tv_login')]")
    username_input = (By.XPATH, "//*[contains(@resource-id,'ti_edittext')[1]]")
    password_input = (By.XPATH, "//*[contains(@resource-id,'text_input_end_icon')]/preceding-sibling::*[last()]")
    login_button = (By.XPATH, "//*[contains(@resource-id,'tv_forgot_password')]/following-sibling::*[position()=1]")
    skip_button = (By.XPATH, "//*[contains(@text,'Skip')]")
    close_button = (By.XPATH, "//*[contains(@text,'New Device')]/preceding-sibling::*[last()]")
    device_picker = (By.XPATH, "//*[contains(@resource-id,'rv_selector_of_device')]")

    def login(self, driver, username: str, password: str) -> None:
        self.find_element_and_click(self.login_button_welcome)
        # self.find_element_and_send_key(self.username_input, username)
        # self.find_element_and_send_key(self.password_input, password)
        self.find_element_and_click(self.login_button)
        self.find_element_and_click(self.skip_button)
        self.find_element_and_click(self.skip_button)
        self.accept_system_alert(driver)
        self.find_element_and_click(self.close_button)
        self.is_element_enabled(self.device_picker)





