from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium:
    def setup(self):
        # 连接调试开关打开的Chrome进程
        # 通过这种方式可以绕过企业微信的登录
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    # 企业微信上传图片
    def test_upload_file(self):
        element_add = self.driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector")
        element_add.click()
        print(self.driver.execute_script("console.log('hello from selenium')"))
        print(self.driver.execute_script("return document.title;"))
        self.driver.execute_script("arguments[0].click();", element_add)
        # self.driver.execute_script("arguments[0].click();",
        #                            self.driver.find_element(By.CSS_SELECTOR, "#js_upload_input"))
        self.driver.find_element(By.CSS_SELECTOR, "#js_upload_input")\
            .send_keys("/Users/feng/package/pythonDemo/images/222.png")
        print(self.driver.page_source)
        # 显示等待,不可见的时候
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel"))
        )
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element_by_css_selector(".js_next"))

    # 使用cookie登录
    def test_cookie(self):
        url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
        self.driver.get(url)
        # 使用无痕模式浏览，比较两次请求的cookie的不同
        cookies = {
            "wwrtx.d2st": "a5373133",
            "wwrtx.sid": "rX_NDIktUTUPXDGK8gDLAyo3q-MAdVxGY7vB3kV5efhXEqgP4urYCEb1cuarkgVw",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324966119483",
            "wxpay.vid": "1688851857778143"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)
        sleep(20)




