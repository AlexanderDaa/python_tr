from fixture.orm import ORMFixture
from fixture.contact import Contact
from fixture.group import Group
import os.path
import random

contact1 = Contact(firstname="addbeforechng", middlename="", lastname="", nickname="",
                   title="", company="", address="", home_phone="1",
                   mobile_phone="11", work_phone="2", fax="32", email="12@22.qq",
                   email2="222@22.qq", email3="332@22.qq", homepage="12.kz", bday="7", bmonth="May",
                   byear="1974", aday="2", amonth="January", ayear="2001", address2="a2, www2",
                   phone2="132", notes="qwey2",
                   photo=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "photo.png"))


def test_add_contacts_to_group(app,orm):
    #db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(orm.get_contact_list()) == 0:
        app.contact.add_new(contact1)
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="addbeforedel", header="", footer=""))
    contact_list_fm_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    #contact_list_fm_hp = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    group_list_fm_db = sorted(orm.get_group_list(), key=Contact.id_or_max)
    #group_list_fm_gp = sorted(app.group.get_group_list(), key=Contact.id_or_max)
    #assert contact_list_fm_hp == contact_list_fm_db
    #assert group_list_fm_gp == group_list_fm_db
    #print(db.get_contact_list())
    #print(db.get_group_list())
    #app.contact.add_contact_to_group_by_id(67,11)
    # пока все работает: добавление контакта 67 в группу 11
    contact_for_add = random.choice(contact_list_fm_db)
    group_to_add = random.choice(group_list_fm_db)
    #print("\n",contact_for_add.id," - контакт")
    #print(group_to_add.id," - группа")
    app.contact.add_contact_to_group_by_id(contact_for_add.id, group_to_add.id)
    # контакт добавляется в группу (если его там нет)
    # получаем список контактов для группы group_to_add
    cont_in_gr = orm.get_contacts_in_group(group_to_add)
    assert contact_for_add in cont_in_gr
    #print(sorted(cont_in_gr, key=Contact.id_or_max))


