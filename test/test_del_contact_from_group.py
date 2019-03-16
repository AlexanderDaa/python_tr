from fixture.contact import Contact
from fixture.group import Group
import os.path
import random
import pytest


contact1 = Contact(firstname="addbeforechng", middlename="", lastname="", nickname="",
                   title="", company="", address="", home_phone="1",
                   mobile_phone="11", work_phone="2", fax="32", email="12@22.qq",
                   email2="222@22.qq", email3="332@22.qq", homepage="12.kz", bday="7", bmonth="May",
                   byear="1974", aday="2", amonth="January", ayear="2001", address2="a2, www2",
                   phone2="132", notes="qwey2",
                   photo=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "photo.png"))


def test_del_contacts_from_group(app,orm):
    with pytest.allure.step('Given a non-empty contact list'):
        if len(orm.get_contact_list()) == 0: # контакты есть
            app.contact.add_new(contact1)
    with pytest.allure.step('Given a non-empty group list'):
        if len(orm.get_group_list()) == 0: # группы есть
            app.group.create(Group(name="addbeforedel", header="", footer=""))
    with pytest.allure.step('Get db group list'):
        group_list_fm_db = orm.get_group_list()
    with pytest.allure.step('Get random group'):
        group_to_del_cont = random.choice(group_list_fm_db)
    with pytest.allure.step('Get non-empty contact list from group %s' % group_to_del_cont):
        cont_in_gr = orm.get_contacts_in_group(group_to_del_cont)
        # если в выбранной группе нет контактов, добавляем туда контакт (что бы было что удалить)
        if len(cont_in_gr) == 0:
            contact_list_fm_db = orm.get_contact_list()
            contact_for_add = random.choice(contact_list_fm_db)
            app.contact.add_contact_to_group_by_id(contact_for_add.id, group_to_del_cont.id)
            cont_in_gr = orm.get_contacts_in_group(group_to_del_cont)
	#предусловия соблюдены (есть откуда и что удалять), можно удалять
    #выбираем контакт из уже выбранной группы
    with pytest.allure.step('Get random contact from list'):
        cont_to_del = random.choice(cont_in_gr)
        #print(cont_to_del," - ",cont_to_del.id)
        #print(group_to_del_cont," - ",group_to_del_cont.id)
        assert cont_to_del in orm.get_contacts_in_group(group_to_del_cont)
    # метод по удалению котакта по id группы и id контакта
    with pytest.allure.step('Remove contact %s from group %s' % (cont_to_del,group_to_del_cont)):
        app.contact.del_contact_fm_group_by_id(group_to_del_cont.id, cont_to_del.id)
    with pytest.allure.step('Check contact list of the group that no removed contact'):
        assert cont_to_del not in orm.get_contacts_in_group(group_to_del_cont)



