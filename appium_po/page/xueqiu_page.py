from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.search_page import SearchPage
from appium_po.page.profile_page import ProfilePage


class XueQiuPage:
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "feng"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        caps['noreset'] = True
        caps["automationName"] = "UiAutomator2"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        # 等待元素出现
        # WebDriverWait(self.driver, 60).until(
        #     expected_conditions.visibility_of_element_located((By.ID, 'image_cancel'))
        # )
        # self.driver.find_element(By.ID, "image_cancel").click()
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el1.click()

    def goto_search(self):
        self.driver.find_element_by_id("home_search").click()
        return SearchPage(self.driver)

    def goto_profile(self):
        return ProfilePage()

    def get_ads(self):
        return False
