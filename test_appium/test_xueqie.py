# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "feng"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        caps["automationName"] = "UiAutomator1"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def test_profile(self):
        # el1 = driver.find_element_by_id("com.xueqiu.android:id/ib_close")
        # el1.click()
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el1.click()
        self.driver.find_element_by_id("title_text").click()

    def teardown(self):
        sleep(10)
        self.driver.quit()
