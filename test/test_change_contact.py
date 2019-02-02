# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="addbeforechng", middlename="", lastname="", nickname="",
                                title="", company="", address="", home_phone="1",
                                mobile_phone="11", work_phone="2", fax="32", email="12@22.qq",
                                email2="222@22.qq", email3="332@22.qq", homepage="12.kz", bday="7", bmonth="May",
                                byear="1974", aday="2", amonth="January", ayear="2001", address2="a2, www2",
                                phone2="132", notes="qwey2",
                                photo="C:\_users\Alexander\__kurs\gitP\python_tr\photo.png"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="f_name2", middlename="m_name2", lastname="l_name2", nickname="nick_name2",
                                title="title2", company="company2", address="address2, qqq2", home_phone="12-12-122",
                                mobile_phone="111-121-12-122", work_phone="23-23-232", fax="34-34-342", email="1112@222.qq",
                                email2="2222@222.qq", email3="3332@222.qq", homepage="1232.kz", bday="7", bmonth="May",
                                byear="1974", aday="2", amonth="January", ayear="2001", address2="address2, www2",
                                phone2="1232", notes="qwerty2",
                                photo="C:\_users\Alexander\__kurs\gitP\python_tr\photo.png")
    contact.id = old_contacts[0].id
    app.contact.change_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_firstname(app):
#    if app.contact.count() == 0:
#        app.contact.add_new(Contact(firstname="addbeforechng"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.change_first_contact(Contact(firstname="f_name2_mod"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)