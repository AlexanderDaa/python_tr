# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=3
f="data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



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


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(test_data_C))


