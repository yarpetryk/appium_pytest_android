import pytest
from pages.profile_page import ProfilePage
from helpers.api_client import ApiClientBasicAuth
import cv2  # pip install opencv-python
import numpy as np


class TestDeviceAmount:
    api_client: ApiClientBasicAuth
    profile_page: ProfilePage

    @pytest.fixture(autouse=True)
    def set_up(self, driver):
        self.api_client = ApiClientBasicAuth()
        self.profile_page = ProfilePage(driver)


    @pytest.mark.smoke
    def test_device_amount(self, driver):
        api_device_counter = len(self.api_client.send_get_request(path='/devices').json())
        self.profile_page.proceed_to_profile_page()
        assert self.profile_page.validate_device_counter(counter=api_device_counter)










