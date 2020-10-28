from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(3)
        self.wd.set_window_size(1920,1080)

    def logout(self):
        wd = self.wd
        el = wd.find_element_by_link_text('Logout')
        el.click()

    def create_group(self, groups):
        wd = self.wd
        #Click new group button
        el = wd.find_element_by_css_selector('input[name="new"]:nth-of-type(1)')
        el.click()

        #Enter value in fields
        el = wd.find_element_by_name('group_name')
        el.send_keys(groups.name)
        el = wd.find_element_by_name('group_header')
        el.send_keys(groups.header)
        el = wd.find_element_by_name('group_footer')
        el.send_keys(groups.footer)

        #Submit
        el = wd.find_element_by_css_selector("input[type=submit]")
        el.click()

    def open_group_page(self):
        wd = self.wd
        el = wd.find_element_by_link_text('groups')
        el.click()

    def login(self, name, password):
        wd = self.wd
        #Enter login
        el = wd.find_element_by_css_selector('input:nth-of-type(1)')
        el.send_keys(name)

        #Enter password
        el = wd.find_element_by_css_selector('input:nth-of-type(2)')
        el.send_keys(password)

        #Click button Login
        el = wd.find_element_by_css_selector('input[type="submit"]')
        el.click()

    def open_home_page(self):
        wd = self.wd
        wd.get('http://localhost/addressbook')

    def destroy(self):
        wd = self.wd
        wd.quit()