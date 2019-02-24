# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db,check_ui, json_contacts):
    contact = json_contacts
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="addbeforechng", middlename="mmm", lastname="lll", nickname="nnn"))
    old_contacts = db.get_contact_list()
    contact_to_ch = random.choice(old_contacts)
    app.contact.change_contact_by_id(contact_to_ch.id, contact)
    new_contacts = db.get_contact_list()
    contact.id=contact_to_ch.id
    old_contacts[old_contacts.index(contact_to_ch)] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        print("check_ui")



