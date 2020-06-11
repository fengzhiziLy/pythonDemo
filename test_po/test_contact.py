from time import sleep, time

from selenium import webdriver

from test_po.contact_page import ContactPage
from test_po.wework_page import Wework


class TestContact:
    def setup(self):
        self.work = Wework()
        self.contact = ContactPage(self.work)

    def teardown(self):
        sleep(10)
        self.work.quit()

    def test_add_member(self):
        self.contact.add_member("feng", "feng", "feng", "12222222222")
        assert self.contact.get_tips() == "OK"

    def test_delete(self):
        udid = str(time())
        self.contact\
            .add_member("x" + udid, "x" + udid, "x_1" + udid, "111111111")

    def test_update_profile(self):
        self.contact.search("xiao").update(name="xiao %s" % str(time()))



