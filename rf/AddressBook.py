import pytest
from fixture.application import Application
import json
import os.path
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self,config="target.json",browser="firefox"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser = self.browser, base_url=web_config["baseUrl"])
        self. fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config["host"],name=db_config["name"],user=db_config["user"],password=db_config["password"])

    def destroy_fixtures(self):
        self.fixture.destroy()
        self.dbfixture.destroy()



    def new_group(self,name,header,footer):
        return Group(name=name,header=header,footer=footer)

    def new_groupWithID(self,group,name,header,footer):
        return Group(id=group.id,name=name,header=header,footer=footer)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def create_group(self,group):
        self.fixture.group.create(group)

    def group_lists_should_be_equal(self,list1,list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def delete_group(self,group):
        self.fixture.group.delete_group_by_id(group.id)

    def modify_group(self,group):
        self.fixture.group.change_group_by_id(group.id,group)



    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def new_contact(self,lastname, firstname, address, email, email2, email3, home_phone, mobile_phone, work_phone, phone2):
        return Contact(lastname=lastname, firstname=firstname, address=address, email=email, email2=email2,
                       email3=email3,home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2)

    def new_contactWithID(self,contact, lastname, firstname, address, email, email2, email3, home_phone, mobile_phone, work_phone, phone2):
        return Contact(id=contact.id, lastname=lastname, firstname=firstname, address=address, email=email, email2=email2,
                       email3=email3,home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2)

    def create_contact(self, new_contact):
        self.fixture.contact.add_new(new_contact)

    def contact_lists_should_be_equal(self,list1,list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def delete_contact(self,contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def modify_contact(self,contact):
        self.fixture.contact.change_contact_by_id(contact.id,contact)