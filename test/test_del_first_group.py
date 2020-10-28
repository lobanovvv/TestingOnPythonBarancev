# -*- coding: utf-8 -*-

from selenium import webdriver
from model.groups import Groups

def test_delete_first_group(app):
    app.open_home_page()
    app.session.login(name='admin', password='secret')
    app.group.open_group_page()
    app.group.delete_first_group()
    app.session.logout()
