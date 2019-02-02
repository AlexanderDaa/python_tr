from selenium.webdriver.support.ui import Select
from model.contact import Contact

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

    def fill_contact_form(self,contact):
        wd = self.app.wd
        if contact.firstname:
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename:
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
        if contact.lastname:
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname:
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        #if contact.photo:
            # wd.find_element_by_name("photo").clear()
            # wd.find_element_by_name("photo").send_keys(contact.photo)
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
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        if contact.byear:
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.byear)
        if contact.aday:
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
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
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                l_name = element.find_element_by_css_selector("td:nth-child(2)").text
                f_name = element.find_element_by_css_selector("td:nth-child(3)").text
                self.contact_cache.append(Contact(id=id, firstname=f_name, lastname=l_name))
                #print(id)
                #print(l_name)
                #print(f_name)
        return list(self.contact_cache)















