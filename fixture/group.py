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
        wd.find_element_by_css_selector('input[name="new"]:nth-of-type(1)').click()

        #Enter value in fields
        wd.find_element_by_name('group_name').send_keys(groups.name)
        wd.find_element_by_name('group_header').send_keys(groups.header)
        wd.find_element_by_name('group_footer').send_keys(groups.footer)

        #Submit
        wd.find_element_by_css_selector("input[type=submit]").click()
    
    def delete_first_group(self):
        wd = self.app.wd
        #Select first element
        wd.find_element_by_name('selected[]').click()
        #Delete element
        wd.find_element_by_name('delete').click()