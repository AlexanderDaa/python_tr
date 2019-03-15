
from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <lastname>,<firstname>,<address>,<email>,<email2>,<email3>,<home_phone>,<mobile_phone>,<work_phone> and <phone2>')
def new_contact(lastname,firstname,address,email,email2,email3,home_phone,mobile_phone,work_phone,phone2):
    return Contact(lastname=lastname,firstname=firstname,address=address,email=email,email2=email2,email3=email3,
                   home_phone=home_phone,mobile_phone=mobile_phone,work_phone=work_phone,phone2=phone2)

@when('I add the contact')
def add_new_contact(app,new_contact):
    app.contact.add_new(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db,contact_list,new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#----------------------------

@given('a non-empty contact list')
def non_empty_contact_list(db,app):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(lastname="l_name"))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact')
def delete_contact(app,random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) -1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert sorted(old_contacts,key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        print("check_ui")
#-------------------------------------------

@when('I change the contact')
def change_contact(app,random_contact, new_contact):
    app.contact.change_contact_by_id(random_contact.id, new_contact)

@then('the new list is equal to the old list with changed contact')
def verify_contact_changed(db,non_empty_contact_list, random_contact,new_contact,app,check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    new_contact.id=random_contact.id
    old_contacts[old_contacts.index(random_contact)] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        print("check_ui")




