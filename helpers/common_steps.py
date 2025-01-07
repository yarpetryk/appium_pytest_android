from helpers.adb_commands import ADB
import time
from helpers.config_handler import Config


class MobileActions:
    def __init__(self):
        self.config_importer = Config()
        self.adb = ADB()
        self.package_name = self.config_importer.get_config('package_name')

    def uninstall_app(self, driver):
        driver.remove_app(self.package_name)

    def terminate_app(self, driver):
        driver.terminate_app(self.package_name)

    def is_installed(self, driver):
        return driver.is_app_installed(self.package_name)

    def activate_app(self, driver):
        driver.activate_app(self.package_name)
        time.sleep(2)

    def clear_data_and_run_app(self, driver):
        self.adb.clear_app_data(self.package_name)
        driver.activate_app(self.package_name)
        time.sleep(2)

    def open_notification(self, driver):
        driver.open_notifications()

    def swipe_down(driver):
        driver.swipe(0, 500, 0, 0)
