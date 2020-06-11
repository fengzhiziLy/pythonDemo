from selenium import webdriver


class Wework:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

        url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
        self.driver.get(url)
        # 使用无痕模式浏览，比较两次请求的cookie的不同
        cookies = {
            "wwrtx.d2st": "a9293053",
            "wwrtx.sid": "rX_NDIktUTUPXDGK8gDLA4T_vRc5MYDnG_D-sfKyd577-ifnOS5RW92KsJQgHt5r",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324966119483",
            "wxpay.vid": "1688851857778143"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)

    def quit(self):
        self.driver.quit()




