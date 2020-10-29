from selenium import webdriver
from fixture.group import GroupHelper
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.wd.set_window_size(1920,1080)

        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get('http://localhost/addressbook')

    def destroy(self):
        wd = self.wd
        wd.quit()

    def is_valid(self):
        wd = self.wd
        try:
            wd.current_url
            return True
        except:
            return False
    