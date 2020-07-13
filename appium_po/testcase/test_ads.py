from appium_po.page.xueqiu_page import XueQiuPage


class TestAds:
    def setup(self):
        self.xueqiu = XueQiuPage()

    def test_ads(self):
        assert self.xueqiu.get_ads() == True
