# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data_G = [Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer",20))
    for i in range(5)]


@pytest.mark.parametrize("group", test_data_G, ids=[repr(x) for x in test_data_G])
def test_modify_group(app, group):
    if app.group.count() == 0:
        app.group.create(Group(name="a", header="b", footer="c"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    print(index)
    group.id = old_groups[index].id
    app.group.change_group_by_index(index,  group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Newname"))
#    old_groups = app.group.get_group_list()
#    app.group.change_first_group(Group(name="Newname2"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="Newheader"))
#    old_groups = app.group.get_group_list()
#    app.group.change_first_group(Group(header="Newheader2"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
