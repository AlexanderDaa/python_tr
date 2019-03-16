
import re
from random import randrange
from fixture.contact import Contact
import os.path
import pytest


contact1 = Contact(firstname="addbeforechng", middlename="", lastname="", nickname="",
                   title="", company="", address="", home_phone="1",
                   mobile_phone="11", work_phone="2", fax="32", email="12@22.qq",
                   email2="222@22.qq", email3="332@22.qq", homepage="12.kz", bday="7", bmonth="May",
                   byear="1974", aday="2", amonth="January", ayear="2001", address2="a2, www2",
                   phone2="132", notes="qwey2",
                   photo=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "photo.png"))


def test_phones_on_home_page(app):
    with pytest.allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.add_new(contact1)
    with pytest.allure.step('Get random contact'):
        index = randrange(app.contact.count())
        #print(str(index))
    with pytest.allure.step('Get data from HP for contact'):
        contact_from_home_page = app.contact.get_contact_list()[index]
    with pytest.allure.step('Get data from EP for contact'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with pytest.allure.step('Check equal phones'):
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    with pytest.allure.step('Check equal names'):
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    with pytest.allure.step('Check equal address'):
        assert contact_from_home_page.address == contact_from_edit_page.address
    with pytest.allure.step('Check equal emails'):
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    with pytest.allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.add_new(contact1)
    with pytest.allure.step('Get random contact'):
        index = randrange(app.contact.count())
        #print(str(index))
    with pytest.allure.step('Get data from VP for contact'):
        contact_from_view_page = app.contact.get_contact_from_view_page(index)
    with pytest.allure.step('Get data from EP for contact'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with pytest.allure.step('Check equal phones'):
        assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
        assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
        assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
        assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!='',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    ([contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2])))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!='',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    ([contact.email, contact.email2, contact.email3])))))


def test_all_phones_on_home_page(app,orm):
    with pytest.allure.step('Given a non-empty contact list'):
        if len(orm.get_contact_list()) == 0:
            app.contact.add_new(contact1)
    with pytest.allure.step('Get data from db for contact'):
        contact_list_fm_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    with pytest.allure.step('Get data from HP for contact'):
        contact_list_fm_hp = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        #print(contact_list_fm_db)
        #print(contact_list_fm_hp)
    with pytest.allure.step('Check that contact lists from db and HP is equal'):
        assert contact_list_fm_db == contact_list_fm_hp
        ii=-1
        for i in contact_list_fm_db:
            ii=ii+1
            #print(i.home_phone, " ", i.work_phone, " ", i.mobile_phone," ",i.phone2)
            #print(i.email, " ",i.email2, " ",i.email3)
            #print(i)
            #print(contact_list_fm_hp[ii])
            assert contact_list_fm_hp[ii].firstname == i.firstname
            assert contact_list_fm_hp[ii].lastname == i.lastname
            assert contact_list_fm_hp[ii].address == i.address
            #print(contact_list_fm_hp[ii].all_emails_from_home_page)
            #print(i.email,'\n',i.email2,'\n',i.email3)
            #print(merge_emails_like_on_home_page(i))
            #print(contact_list_fm_hp[ii].all_phones_from_home_page)
            assert contact_list_fm_hp[ii].all_emails_from_home_page == merge_emails_like_on_home_page(i)
            assert contact_list_fm_hp[ii].all_phones_from_home_page == merge_phones_like_on_home_page(i)
        print("%s contacts checked" % ii)

