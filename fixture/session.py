class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, name, password):
        wd = self.app.wd
        #Enter login
        wd.find_element_by_css_selector('input:nth-of-type(1)').send_keys(name)

        #Enter password
        wd.find_element_by_css_selector('input:nth-of-type(2)').send_keys(password)

        #Click button Login
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Logout').click()
