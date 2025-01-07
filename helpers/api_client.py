import requests
from requests import Response
from requests.auth import HTTPBasicAuth
from helpers.secure_config_handler import SecureConfig


class ApiClientBasicAuth:
    def __init__(self):
        self.api_config = SecureConfig()
        self.base_url = self.api_config.get_config().get("base_url")
        self.auth = HTTPBasicAuth(self.api_config.get_config().get("login"),
                                  self.api_config.get_config().get("password"))

    def send_get_request(self, path: str, timeout=10) -> Response or None:
        print(self.base_url)
        request_path = self.base_url + path
        response = requests.get(request_path, auth=self.auth, timeout=timeout)
        return response

    def send_post_request(self, path: str, body: str, timeout=10) -> Response:
        request_path = self.base_url + path
        try:
            response = requests.post(request_path, auth=self.auth, json=body, timeout=timeout)
        except requests.Timeout as exception:
            response = None
            print("Timeout waiting for response to get request to "
                  f"{request_path} - {exception}")
        return response
