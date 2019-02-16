# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path


constant = [
    Contact(firstname="fname1", middlename="mname1", lastname="lname1",
            nickname="nname1", title="title", company="company",
            address="address", home_phone="hphone1", mobile_phone="mphone1",
            work_phone="wphone1", fax="fax", email="email1_",
            email2="email2_", email3="email3_", homepage="hpage",
            bday=random.choice('123456789'), bmonth='April', byear='1973', aday=random.choice('123456789'),
            amonth="January", ayear="2000", address2="address2_",phone2="phone2_",
            notes="notes", photo=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..","photo.png")),
    Contact(firstname="fname2", middlename="mname2", lastname="lname2",
            nickname="nname2", title="title", company="company",
            address="address", home_phone="hphone2", mobile_phone="mphone2",
            work_phone="wphone2", fax="fax", email="email1_",
            email2="email2_", email3="email3_", homepage="hpage",
            bday=random.choice('123456789'), bmonth='April', byear='1973', aday=random.choice('123456789'),
            amonth="January", ayear="2000", address2="address2_", phone2="phone2_",
            notes="notes", photo=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..","photo.png"))
]



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data_C = [
    Contact(firstname=random_string("fname",10), middlename=random_string("mname",10), lastname=random_string("lname",10),
            nickname=random_string("nname",10), title=random_string("title",10), company=random_string("company",10),
            address=random_string("address",10), home_phone=random_string("hphone",10), mobile_phone=random_string("mphone",10),
            work_phone=random_string("wphone",10), fax=random_string("fax",10), email=random_string("email1_",10),
            email2=random_string("email2_",10), email3=random_string("email3_",10), homepage=random_string("hpage",10),
            bday=random.choice('123456789'), bmonth='April', byear='1973', aday=random.choice('123456789'),
            amonth="January", ayear="2000", address2=random_string("address2_",10),phone2=random_string("phone2_",10),
            notes=random_string("notes",10), photo="C:\_users\Alexander\__kurs\gitP\python_tr\photo.png")
    for i in range(3)]

