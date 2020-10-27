# -*- coding: utf-8 -*-

from selenium import webdriver
from random import shuffle
import time, unittest

class test_add_group(unittest.TestCase):

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, name='admin', password='secret')
        self.open_group_page(wd)
        self.create_group(wd, name="a", header="a", footer="a")
        self.logout(wd)

    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(3)
        self.wd.set_window_size(1920,1080)

    def logout(self, wd):
        el = wd.find_element_by_link_text('Logout')
        el.click()

    def create_group(self, wd, name, header, footer):
        #Click new group button
        el = wd.find_element_by_css_selector('input[name="new"]:nth-of-type(1)')
        el.click()

        #Enter value in fields
        el = wd.find_element_by_name('group_name')
        el.send_keys(name)
        el = wd.find_element_by_name('group_header')
        el.send_keys(header)
        el = wd.find_element_by_name('group_footer')
        el.send_keys(footer)

        #Submit
        el = wd.find_element_by_css_selector("input[type=submit]")
        el.click()

    def open_group_page(self, wd):
        el = wd.find_element_by_link_text('groups')
        el.click()

    def login(self, wd, name, password):
        #Enter login
        time.sleep(1)
        el = wd.find_element_by_css_selector('input:nth-of-type(1)')
        el.send_keys(name)

        #Enter password
        el = wd.find_element_by_css_selector('input:nth-of-type(2)')
        el.send_keys(password)

        #Click button Login
        el = wd.find_element_by_css_selector('input[type="submit"]')
        el.click()

    def open_home_page(self, wd):
        wd.get('http://localhost/addressbook')

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()