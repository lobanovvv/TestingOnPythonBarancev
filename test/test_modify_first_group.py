# -*- coding: utf-8 -*-

from selenium import webdriver
from model.groups import Groups

def test_delete_first_group(app):
    app.open_home_page()
    app.session.login(name='admin', password='secret')
    app.group.open_group_page()
    app.group.select_first_element()
    app.group.click_to_edit_button()
    app.group.change_all_value(Groups(name = 'AASDFSD Name'))
    app.session.logout()
