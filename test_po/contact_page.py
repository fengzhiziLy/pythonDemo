from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import BasePage
from test_po.profile_page import ProfilePage


class ContactPage(BasePage):
    _username = (By.NAME, "username")
    _alias = (By.NAME, "english_name")
    _id = (By.NAME, "acctid")
    _mobile = (By.NAME, "mobile")
    _cancel = (By.CSS_SELECTOR, ".js_btn_cancel")
    _leave = (By.XPATH, "//*[text()='离开此页']")
    _search = (By.ID, "memberSearchInput")
    _add = (By.CSS_SELECTOR, ".js_has_member .ww_operationBar .js_add_member")

    def __init__(self, wework):
        self.driver = wework.driver

    def add_member(self, name, alias, id, mobile, **kwargs):
        # locator = ".js_has_member .ww_operationBar .js_add_member"
        WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            expected_conditions.element_to_be_clickable(*self._add))

        sleep(3)
        # print("3s")
        # for index in range(10):
        #     print(self.driver.find_element_by_css_selector(locator).location)
        #     sleep(0.5)
        self.click_by_js(By.CSS_SELECTOR, ".js_add_member")
        self.find(self._username).send_keys(name)
        self.find(*self._alias).send_keys(alias)
        self.find(self._id).send_keys(id)
        self.find(*self._mobile).send_keys(mobile)
        self.click_by_js(*self._cancel)
        self.click_by_js(*self._leave)

    def delete_member(self):
        pass

    def get_tips(self):
        return "OK"

    def search(self, key):
        self.driver.find_element(*self._search).send_keys(key)
        return ProfilePage(self.driver)





