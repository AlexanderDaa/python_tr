# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.change_first_group(Group(name="group123 changed", header="header123 changed", footer="footer123 changed"))
