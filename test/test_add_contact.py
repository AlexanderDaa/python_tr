# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.contacts import constant as test_data_C


@pytest.mark.parametrize("contact", test_data_C, ids=[repr(x) for x in test_data_C])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





