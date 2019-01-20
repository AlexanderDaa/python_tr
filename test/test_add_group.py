# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.manager.session.login(username="admin", password="secret")
    app.manager.group.create(Group(name="group123", header="header123", footer="footer123"))
    app.manager.session.logout()


def test_add_empty_group(app):
    app.manager.session.login(username="admin", password="secret")
    app.manager.group.create(Group(name="", header="", footer=""))
    app.manager.session.logout()
