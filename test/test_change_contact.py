# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.manager.session.login(username="admin", password="secret")
    app.manager.contact.change_first_contact(Contact(firstname="f_name2", middlename="m_name2", lastname="l_name2", nickname="nick_name2",
                                title="title2", company="company2", address="address2, qqq2", home_phone="12-12-122",
                                mobile_phone="111-121-12-122", work_phone="23-23-232", fax="34-34-342", email="1112@222.qq",
                                email2="2222@222.qq", email3="3332@222.qq", homepage="1232.kz", bday="7", bmonth="May",
                                byear="1974", aday="2", amonth="January", ayear="2001", address2="address2, www2",
                                phone2="1232", notes="qwerty2",
                                photo="C:\_users\Alexander\__kurs\gitP\python_tr\photo.png"))
    app.manager.session.logout()
