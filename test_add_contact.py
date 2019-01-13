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
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("f_name")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("m_name")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("l_name")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("nick_name")
        driver.find_element_by_name("photo").click()
        driver.find_element_by_name("photo").clear()
        driver.find_element_by_name("photo").send_keys("C:\\fakepath\\photo.png")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("title")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("company")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("address, qqq")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("12-12-12")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("111-121-12-12")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("23-23-23")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("34-34-34")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("111@222.qq")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("222@222.qq")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("333@222.qq")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("123.kz")
        Select(driver.find_element_by_name("bday")).select_by_visible_text("6")
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("April")
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1973")
        Select(driver.find_element_by_name("aday")).select_by_visible_text("1")
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("January")
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2000")
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("address, www")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("123")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("qwerty")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
