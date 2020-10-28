# -*- coding: utf-8 -*-

from selenium import webdriver
from groups import Groups
from application import Application
import time, pytest

@pytest.fixture()
def app():
    fixture = Application()
    return fixture

def test_add_group(app):
    app.open_home_page()
    app.login(name='admin', password='secret')
    app.open_group_page()
    app.create_group(Groups(name="b", header="b", footer="b"))
    app.logout()

if __name__ == '__main__':
    pytest.main()