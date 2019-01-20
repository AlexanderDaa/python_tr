# -*- coding: utf-8 -*-


def test_add_contact(app):
    app.manager.session.login(username="admin", password="secret")
    app.manager.contact.delete_first_contact()
    app.manager.session.logout()
