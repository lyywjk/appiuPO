from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from PO_lianx.page.Basege import Basege
from PO_lianx.page.main import MianPage


class App(Basege):
    driver: WebDriver

    def start(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def close(self):
        pass

    def main(self):
        return MianPage(self.driver)
