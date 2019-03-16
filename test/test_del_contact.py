# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import os.path
import pytest

def test_del_contact(app, db, check_ui):
    with pytest.allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.add_new(Contact(firstname="addbeforedel", middlename="", lastname="", nickname="",
                                    title="", company="", address="", home_phone="1",
                                    mobile_phone="11", work_phone="2", fax="32", email="12@22.qq",
                                    email2="222@22.qq", email3="332@22.qq", homepage="12.kz", bday="7", bmonth="May",
                                    byear="1974", aday="2", amonth="January", ayear="2001", address2="a2, www2",
                                    phone2="132", notes="qwey2",
                                    photo=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "photo.png")))
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with pytest.allure.step('When I delete the contact %s' % contact):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step('Then the new list is equal to the old list without the deleted contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) -1 == len(new_contacts)
        old_contacts.remove(contact)
        assert sorted(old_contacts,key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
            print("check_ui")



