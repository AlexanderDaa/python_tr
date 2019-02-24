# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import os.path


test_data = [Contact(firstname="",middlename="", lastname="")]+[
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

