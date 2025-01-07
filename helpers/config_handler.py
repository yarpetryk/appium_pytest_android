import json


CONFIG_PATH = "./configs/config.json"


class Config:
    def __init__(self):
        self.config_value = None

    def get_config(self, config):
        with open(CONFIG_PATH, 'r') as config_file:
            data = json.load(config_file)
            if config in data.keys():
                self.config_value = data[config]
            else:
                raise Exception(config + " is missing")
        return self.config_value
