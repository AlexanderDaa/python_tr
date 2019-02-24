# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db,check_ui,json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_new(contact)
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        print("check_ui")





