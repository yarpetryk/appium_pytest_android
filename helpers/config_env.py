import os
from dotenv import load_dotenv
from helpers.config_importer import ConfigImporter


class EnvConfig:
    def __init__(self):
        self.config_importer = ConfigImporter()
        self.env_path = self.config_importer.get_config('config_env_file')

    def get_config(self):
        load_dotenv(dotenv_path=self.env_path)
        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")
        base_url = os.getenv("BASE_URL")
        return {
            "login": login,
            "password": password,
            "base_url": base_url
        }
