import pytest
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from helpers.api_client import ApiClientBasicAuth
from helpers.config_env import EnvConfig
from helpers.common_steps import MobileActions


class TestDeviceAmount:
    # Setting up the initialization
    def init(self):
        self.login_page = LoginPage()
        self.profile_page = ProfilePage()
        self.api_client = ApiClientBasicAuth()
        self.mobile_command = MobileActions()
        self.env_config = EnvConfig()
        self.username = self.env_config.get_config['login']
        self.password = self.env_config.get_config['password']
        self.apiUrl = self.env_config.get_config['base_url']

    # Mark test as a "power_operating" to run marked tests in the future
    @pytest.mark.smoke
    def test_device_amount(self, driver):
        #  Initialization
        self.init()
        self.mobile_command.clear_data_and_run_app(driver)

        self.login_page.login(username=self.username,
                              password=self.password)
        assert self.login_page.isUserSignedIn()



        api_device_counter = len(self.api_client.send_get_request(path='/devices'))
        assert self.profile_page.validateDeviceCounter(counter=api_device_counter)





