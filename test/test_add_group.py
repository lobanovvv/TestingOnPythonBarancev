# -*- coding: utf-8 -*-

from selenium import webdriver
from model.groups import Groups
from fixture.application import Application
import time, pytest

def test_add_group(app):
    app.open_home_page()
    app.session.login(name='admin', password='secret')
    app.group.open_group_page()
    app.group.create_group(Groups(name="b", header="b", footer="b"))
    app.session.logout()
