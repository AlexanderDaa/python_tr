import  re
from random import randrange
from fixture.contact import Contact

def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="addbeforechng", middlename="", lastname="", nickname="",
                                title="", company="", address="", home_phone="1",
                                mobile_phone="11", work_phone="2", fax="32", email="12@22.qq",
                                email2="222@22.qq", email3="332@22.qq", homepage="12.kz", bday="7", bmonth="May",
                                byear="1974", aday="2", amonth="January", ayear="2001", address2="a2, www2",
                                phone2="132", notes="qwey2",
                                photo="C:\_users\Alexander\__kurs\gitP\python_tr\photo.png"))
    index = randrange(app.contact.count())
    print(str(index))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="addbeforechng", middlename="", lastname="", nickname="",
                                title="", company="", address="", home_phone="1",
                                mobile_phone="11", work_phone="2", fax="32", email="12@22.qq",
                                email2="222@22.qq", email3="332@22.qq", homepage="12.kz", bday="7", bmonth="May",
                                byear="1974", aday="2", amonth="January", ayear="2001", address2="a2, www2",
                                phone2="132", notes="qwey2",
                                photo="C:\_users\Alexander\__kurs\gitP\python_tr\photo.png"))
    index = randrange(app.contact.count())
    print(str(index))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
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

