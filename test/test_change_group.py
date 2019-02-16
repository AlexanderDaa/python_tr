# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import pytest
from data.groups import constant as test_data_G


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

