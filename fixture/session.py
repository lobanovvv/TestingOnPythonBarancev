class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, name, password):
        wd = self.app.wd
        #Enter login
        el = wd.find_element_by_css_selector('input:nth-of-type(1)')
        el.send_keys(name)

        #Enter password
        el = wd.find_element_by_css_selector('input:nth-of-type(2)')
        el.send_keys(password)

        #Click button Login
        el = wd.find_element_by_css_selector('input[type="submit"]')
        el.click()

    def logout(self):
        wd = self.app.wd
        el = wd.find_element_by_link_text('Logout')
        el.click()
