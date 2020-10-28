class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        el = wd.find_element_by_link_text('groups')
        el.click()

    def create_group(self, groups):
        wd = self.app.wd
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