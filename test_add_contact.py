# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("f_name")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("m_name")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("l_name")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("nick_name")
        wd.find_element_by_name("photo").click()
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys("C:\\fakepath\\photo.png")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("address, qqq")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("12-12-12")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("111-121-12-12")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("23-23-23")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("34-34-34")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("111@222.qq")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("222@222.qq")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("333@222.qq")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("123.kz")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("6")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("April")
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1973")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("address, www")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("123")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("qwerty")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
