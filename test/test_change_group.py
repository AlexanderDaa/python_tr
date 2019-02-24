# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest

def test_modify_group(app, db, check_ui, json_groups):
    group = json_groups
    if app.group.count() == 0:
        app.group.create(Group(name="a", header="b", footer="c"))
    old_groups = db.get_group_list()
    group_to_ch = random.choice(old_groups)
    app.group.change_group_by_id(group_to_ch.id,group)
    new_groups = db.get_group_list()
    group.id = group_to_ch.id
    old_groups[old_groups.index(group_to_ch)]=group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
        print("check_ui")




from random import randrange
@pytest.mark.skip
def test_modify_group_old(app, json_groups):
    group = json_groups
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

