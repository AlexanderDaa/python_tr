# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="addbeforedel", middlename="", lastname="", nickname="",
                                title="", company="", address="", home_phone="1",
                                mobile_phone="11", work_phone="2", fax="32", email="12@22.qq",
                                email2="222@22.qq", email3="332@22.qq", homepage="12.kz", bday="7", bmonth="May",
                                byear="1974", aday="2", amonth="January", ayear="2001", address2="a2, www2",
                                phone2="132", notes="qwey2",
                                photo="C:\_users\Alexander\__kurs\gitP\python_tr\photo.png"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts