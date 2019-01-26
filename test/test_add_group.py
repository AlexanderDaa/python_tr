# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="name", header="header123", footer="footer123"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

