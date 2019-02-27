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
    group_list_fm_db = orm.get_group_list()
    group_to_del_cont = random.choice(group_list_fm_db)
    cont_in_gr = orm.get_contacts_in_group(group_to_del_cont)
    if len(cont_in_gr) == 0:
        contact_list_fm_db = orm.get_contact_list()
        contact_for_add = random.choice(contact_list_fm_db)
        app.contact.add_contact_to_group_by_id(contact_for_add.id, group_to_del_cont.id)
        cont_in_gr = orm.get_contacts_in_group(group_to_del_cont)
#предусловия соблюдены, можно удалять
    cont_to_del = random.choice(orm.get_contacts_in_group(group_to_del_cont))
    print(cont_to_del)
    print(cont_in_gr)
#пока не реализовано
#    app.contact.del_contact_fm_group_by_id(group_to_del_cont.id,cont_to_del.id)


