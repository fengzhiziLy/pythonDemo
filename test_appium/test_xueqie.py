# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from hamcrest import *


class TestXueqiu:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "feng"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        caps["automationName"] = "UiAutomator1"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el1.click()

    def setup(self):
        pass

    def teardown(self):
        self.driver.find_element_by_id("action_close").click()

    def teardown_class(self):
        sleep(10)
        self.driver.quit()

    def test_profile(self):
        # el1 = driver.find_element_by_id("com.xueqiu.android:id/ib_close")
        # el1.click()
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el1.click()
        self.driver.find_element_by_id("title_text").click()

    def test_source(self):
        print(self.driver.page_source)

    def test_selected_delete(self):
        # self.driver.find_elements_by_xpath("//*[@text='行情']").click()
        pass

    def test_swipe(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el1.click()
        for i in range(5):
            self.driver.swipe(500, 900, 100, 200, 1000)

    @pytest.mark.parametrize("keyword, stock_type, expect_price", [
        ('alibaba', 'BABA', 210),
        ('xiaomi', '01810', 13)
    ])
    def test_search(self, keyword, stock_type, expect_price):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='" + stock_type + "']/../../.."
                                                                                 "//*[contains(@resource-id, 'current_price')]").text)
        print(price)
        assert price > expect_price
        assert_that(price, close_to(expect_price, expect_price*0.1))


