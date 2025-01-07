import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from pages.login_page import LoginPage
from helpers.common_steps import MobileActions
from helpers.secure_config_handler import SecureConfig


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    capabilities = {
        'platformName': 'Android',
        'autoGrantPermissions': True
    }
    # ios_capabilities = {
    #     'platformName': 'iOS',
    #     'deviceName': 'iPhone',
    #     'automationName': 'XCuiTest',
    #     'udid': 'auto',
    #     'bundleId': 'energy.powerfox.one'
    # }
    options.load_capabilities(capabilities)
    url = 'http://localhost:4723'
    appium_driver = webdriver.Remote(url, options=options)

    yield appium_driver
    appium_driver.quit()

@pytest.fixture(autouse=True)
def login_set_up(driver):
    login_page = LoginPage(driver)
    mobile_command = MobileActions()
    config = SecureConfig()
    username = config.get_config()['login']
    password = config.get_config()['password']
    mobile_command.clear_data_and_run_app(driver)
    login_page.login(driver=driver, username=username, password=password)



