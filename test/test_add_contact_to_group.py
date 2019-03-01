
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
    if len(orm.get_contact_list()) == 0:
        app.contact.add_new(contact1)
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="addbeforedel", header="", footer=""))
    # выбираем контакт, который будем добавлять
    contact_list_fm_db = orm.get_contact_list()
    contact_for_add = random.choice(contact_list_fm_db)
    # составляем список групп, в которых нет этого контакта
    group_list_fm_db = orm.get_group_list()
    group_list_without_contact_for_add = []
    for gr in group_list_fm_db:
        if contact_for_add not in orm.get_contacts_in_group(gr):
            group_list_without_contact_for_add.append(gr)
    #print(group_list_without_contact_for_add)
    #print(contact_for_add)
	# проверяем список групп, в которых нет выбранного контакта 
	# и выбираем группу, в которую будем его добавлять 
    if len(group_list_without_contact_for_add) == 0:
        # если групп без этого контакта нет, выбираем группу из общего списка и удаляем из нее контакт
        group_to_add = random.choice(group_list_fm_db)
        app.contact.del_contact_fm_group_by_id(group_to_add.id, contact_for_add.id)
        #print("группа выбрана из общего списка групп")
    else:
        # если такие группы есть, выбираем группу из списка групп, в которых нет контакта
        group_to_add = random.choice(group_list_without_contact_for_add)
        #print("группа выбрана из списка групп, в которых нет контакта")
    # получаем список контактов для группы group_to_add
    cont_in_gr = orm.get_contacts_in_group(group_to_add)
    # проверяем, что в группе нет контакта 
    assert contact_for_add not in cont_in_gr
    # контакт добавляем в группу
    app.contact.add_contact_to_group_by_id(contact_for_add.id, group_to_add.id)
    # получаем новый список контактов для группы group_to_add
    cont_in_gr = orm.get_contacts_in_group(group_to_add)
    assert contact_for_add in cont_in_gr
	
	

	
	
	