class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('groups').click()

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
        wd.find_element_by_name('delete').click()

    def select_first_element(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def click_to_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_name('edit').click()

    def change_current_field_value(self, field_name, new_value):
        wd = self.app.wd
        if new_value is not None:
            el = wd.find_element_by_name(field_name)
            el.click()
            el.clear()
            el.send_keys(new_value)

    def change_all_value(self, groups):
        self.change_current_field_value("group_name", groups.name)
        self.change_current_field_value("group_header", groups.header)
        self.change_current_field_value("group_footer", groups.footer)
