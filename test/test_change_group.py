# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.manager.session.login(username="admin", password="secret")
    app.manager.group.change_first_group(Group(name="group123 changed", header="header123 changed", footer="footer123 changed"))
    app.manager.session.logout()