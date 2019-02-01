# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="addbeforechng", header="", footer=""))
    old_groups = app.group.get_group_list()
    group = Group(name="group123 changed", header="header123 changed", footer="footer123 changed")
    group.id = old_groups[0].id
    app.group.change_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
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
