from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select some contact
        wd.find_elements_by_name("selected[]")[index].click()
        # delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # delete confirmation
        wd.switch_to_alert().accept()
        # wait
        wd.implicitly_wait(5)
        wd.find_element_by_css_selector("div.msgbox")
        wd.find_element_by_link_text("Last name")
        self.contact_cache = None

    def add_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def change_first_contact(self, contact):
        self.change_contact_by_index(index=0, contact=contact)

    def change_contact_by_index(self, index, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select some contact
        wd.find_elements_by_name("selected[]")[index].click()
        # click the "edit"
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(contact)
        # update
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd= self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select some contact
        self.select_contact_by_id(id)
        # delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # delete confirmation
        wd.switch_to_alert().accept()
        # wait
        wd.implicitly_wait(5)
        wd.find_element_by_css_selector("div.msgbox")  #проверить на рабочем компе
        wd.find_element_by_link_text("Last name")
        self.contact_cache = None

    def change_contact_by_id(self, id, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select some contact
        self.select_contact_by_id(id)
        # click the "edit"
        #wd.find_elements_by_xpath("//img[@alt='Edit']")[int(id)].click()
        css = "a[href=\"edit.php?id=" + str(id)+"\"] img[title='Edit']"
        #wd.find_element_by_css_selector("a[href=\"edit.php?id=43\"] img[title='Edit']").click()
        wd.find_element_by_css_selector(css).click()
        # fill contact form
        self.fill_contact_form(contact)
        # update
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def fill_contact_form(self,contact):
        wd = self.app.wd
        if not contact.firstname:
            contact.firstname=""
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename:
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
        if not contact.lastname:
            contact.lastname=""
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname:
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        #if contact.photo:
        #    wd.find_element_by_name("photo").clear()
        #    wd.find_element_by_name("photo").send_keys(contact.photo)
        if contact.title:
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)
        if contact.company:
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company)
        if contact.address:
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.home_phone:
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.home_phone)
        if contact.mobile_phone:
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        if contact.work_phone:
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.work_phone)
        if contact.fax:
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contact.fax)
        if contact.email:
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
        if contact.email2:
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3:
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.homepage:
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if contact.bday:
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        if contact.bmonth:
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        if contact.byear:
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.byear)
        if contact.aday:
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        if contact.amonth:
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        if contact.ayear:
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contact.ayear)
        if contact.address2:
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(contact.address2)
        if contact.phone2:
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.phone2)
        if contact.notes:
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(contact.notes)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_contact_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.find_element_by_link_text("home").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                f_name = cells[2].text
                l_name = cells[1].text
                address = cells[3].text
                emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=f_name, lastname=l_name,
                                                  address=address, all_emails_from_home_page = emails,
                                                  all_phones_from_home_page = all_phones))
                #print(id)
                #print(l_name)
                #print(f_name)
                #print(address)
                #print(emails)
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        secondaryphone = wd.find_element_by_name('phone2').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home_phone=homephone, mobile_phone=mobilephone,
                       work_phone=workphone, phone2=secondaryphone,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=homephone, mobile_phone=mobilephone,
                       work_phone=workphone, phone2=secondaryphone)


    def add_contact_to_group_by_id(self,id_c,id_gr):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id_c)
        wd.find_element_by_name("to_group").click()
        #Select(driver.find_element_by_css_selector("select[name=\"to_group\"]")).select_by_visible_text("namegru")
        wd.find_element_by_css_selector("select[name=\"to_group\"] > option[value=\"%s\"]" % id_gr).click()
        wd.find_element_by_css_selector("input[name=\"add\"]").click()
        wd.implicitly_wait(5)
        wd.find_element_by_css_selector("i > a").click()

    def del_contact_fm_group_by_id(self, id_gr, id_cont):
        pass


        #driver = self.driver
        #driver.get("http://localhost/addressbook/")
        #driver.find_element_by_css_selector("select[name=\"group\"]").click()
        #Select(driver.find_element_by_name("group")).select_by_visible_text("namegru")
        #driver.find_element_by_css_selector("option[value=\"11\"]").click()
        #driver.find_element_by_css_selector("#67").click()
        #driver.find_element_by_css_selector("input[name=\"remove\"]").click()
        #driver.find_element_by_link_text("home").click()
        #driver.find_element_by_css_selector("select[name=\"group\"]").click()
        #Select(driver.find_element_by_name("group")).select_by_visible_text("[all]")
        #driver.find_element_by_xpath("//option[@value='']").click()






