# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest

def test_modify_contact(app, db,check_ui, json_contacts):
    contact = json_contacts
    with pytest.allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.add_new(Contact(firstname="addbeforechng", middlename="mmm", lastname="lll", nickname="nnn"))
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from the list'):
        contact_to_ch = random.choice(old_contacts)
    with pytest.allure.step('When I change the contact %s' % contact_to_ch):
        app.contact.change_contact_by_id(contact_to_ch.id, contact)
    with pytest.allure.step('Then the new list is equal to the old list with changed contact'):
        new_contacts = db.get_contact_list()
        contact.id=contact_to_ch.id
        old_contacts[old_contacts.index(contact_to_ch)] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
            print("check_ui")



