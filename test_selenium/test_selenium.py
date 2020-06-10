import logging
from time import sleep, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)


class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(20)
        self.driver.get('https://testerhome.com/')

    def teardown(self):
        self.driver.quit()

    # def test_browser(self):
    #     self.driver.get('https://testerhome.com/')

    def test_search(self):
        search = self.driver.find_element_by_name("q")
        search.send_keys("selenium")
        sleep(20)

    def test_0609(self):
        search = self.driver.find_element_by_name("q")
        search.send_keys("先到先得")
        self.driver.find_element_by_name("q").submit()
        sleep(3)
        # self.driver.find_element(By.CSS_SELECTOR, '.title [title*="Android 端测试基础知识分享"]').click()
        # self.driver.find_element(By.XPATH, '//a[contains(text(), "adb查看设备信息")]').click()
        # self.driver.find_element(By.CSS_SELECTOR, '第五届中国移动互联网测试开发大会 ').click()
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[1]/a').click()
        sleep(5)
        self.driver.find_element(By.XPATH, '//p[contains(text(), "问卷")]/a').click()
        for w in self.driver.window_handles:
            logging.info(w)
            self.driver.switch_to.window(w)
            logging.info(self.driver.title)
        sleep(5)
        # for w in self.driver.window_handles:
        #     logging.info(w)
        #     self.driver.switch_to.window(w)
        #     logging.info(self.driver.title)

    def test_explicit_wait(self):
        self.driver.find_element_by_partial_link_text("社区").click()
        self.driver.find_element_by_partial_link_text("最新发布").click()
        logging.info(time())
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".topic .title a"))
        )
        logging.info((time()))
