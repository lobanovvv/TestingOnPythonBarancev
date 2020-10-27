# -*- coding: utf-8 -*-

from selenium import webdriver
from random import shuffle
import time, unittest

class test_add_group(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(3)
        self.wd.set_window_size(1920,1080)
        self.wd.get('http://localhost/addressbook')

    def test_add_group(self):
        wd = self.wd
        #LOGIN
        #Enter login
        time.sleep(1)
        el = wd.find_element_by_css_selector('input:nth-of-type(1)')
        el.send_keys('admin')

        #Enter password
        el = wd.find_element_by_css_selector('input:nth-of-type(2)')
        el.send_keys('secret')

        #Click button Login
        el = wd.find_element_by_css_selector('input[type="submit"]')
        el.click()


        #GROUP
        #Jump to group tab
        el = wd.find_element_by_link_text('groups')
        el.click()

        #Create new group
        el = wd.find_element_by_css_selector('input[name="new"]:nth-of-type(1)')
        el.click()

        #Enter value in fields
        el_name = [
            'input[name="group_name"]',
            'textarea[name="group_header"]',
            'textarea[name="group_footer"]'
        ]
        abcdefg = ['a', 'b', 'c', 'd', 'e', 'f','g']

        for i in el_name:
            el = wd.find_element_by_css_selector(i)
            shuffle(abcdefg)
            el.send_keys(abcdefg)

        #Submit
        el = wd.find_element_by_css_selector("input[type=submit]")
        el.click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()