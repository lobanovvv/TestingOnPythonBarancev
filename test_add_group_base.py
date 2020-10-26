from selenium import webdriver
import time
from random import shuffle

wd = webdriver.Chrome()
wd.implicitly_wait(3)
wd.set_window_size(1920,1080)
wd.get('http://localhost/addressbook')

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

wd.quit()
