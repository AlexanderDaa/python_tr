# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data_C = [
    Contact(firstname=random_string("fname",10), middlename=random_string("mname",10), lastname=random_string("lname",10),
            nickname=random_string("nname",10), title=random_string("title",10), company=random_string("company",10),
            address=random_string("address",10), home_phone=random_string("hphone",10), mobile_phone=random_string("mphone",10),
            work_phone=random_string("wphone",10), fax=random_string("fax",10), email=random_string("email1_",10),
            email2=random_string("email2_",10), email3=random_string("email3_",10), homepage=random_string("hpage",10),
            bday=random.choice('123456789'), bmonth='April', byear='1973', aday=random.choice('123456789'),
            amonth="January", ayear="2000", address2=random_string("address2_",10),phone2=random_string("phone2_",10),
            notes=random_string("notes",10), photo="C:\_users\Alexander\__kurs\gitP\python_tr\photo.png")
    for i in range(5)]


@pytest.mark.parametrize("contact", test_data_C, ids=[repr(x) for x in test_data_C])
def test_modify_contact(app, contact):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="addbeforechng", middlename="mmm", lastname="lll", nickname="nnn"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.change_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

