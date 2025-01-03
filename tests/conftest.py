import pytest
from appium import webdriver
from helpers.config_importer import ConfigImporter


config_importer = ConfigImporter()

@pytest.fixture(scope="session")
def driver():
    locale = str(config_importer.config_locale())
    language = str(config_importer.config_language())
    capabilities = {
        'platformName': 'Android',
        'language': language,
        'locale': locale
    }
    url = 'http://localhost:4723/wd/hub'
    appium_driver = webdriver.Remote(url, capabilities)

    yield appium_driver
    appium_driver.quit()

