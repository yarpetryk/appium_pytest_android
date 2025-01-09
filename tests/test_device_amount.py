import pytest
from pages.profile_page import ProfilePage
from helpers.api_client import ApiClientBasicAuth
from helpers.image_handler import Image


class TestDeviceAmount:
    api_client: ApiClientBasicAuth
    profile_page: ProfilePage
    image_handler: Image

    @pytest.fixture(autouse=True)
    def set_up(self, driver):
        self.api_client = ApiClientBasicAuth()
        self.profile_page = ProfilePage(driver)
        self.image_handler = Image()


    @pytest.mark.smoke
    def test_device_amount(self, driver):
        api_device_counter = len(self.api_client.send_get_request(path='/devices').json())
        self.profile_page.proceed_to_profile_page()
        assert self.profile_page.validate_device_counter(counter=api_device_counter)

        driver.get_screenshot_as_file("./results/expected.png")
        driver.get_screenshot_as_file("./results/actual.png")
        assert self.image_handler.compare_images(expected='./results/expected.png',
                                                 actual='./results/actual.png',
                                                 result='./results/result.png')










