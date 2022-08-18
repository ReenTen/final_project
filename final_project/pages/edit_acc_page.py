from final_project.pages.base_page import BasePage
from final_project.locators.edit_acc_page_loc import EditAccPageLoc
from final_project.database_request import check_changing_user_name


class EditAccPage(BasePage):

    def check_edit_account_page_url(self):
        assert self.chrome.current_url == EditAccPageLoc.edit_acc_page_url,\
            'Edit account page URL is not equall recieved link!'

    def check_first_name_field(self):
        assert self.element_search_and_use(EditAccPageLoc.first_name_field_loc),\
            'First name field isn\'t present on this page!'

    def check_last_name_field(self):
        assert self.element_search_and_use(EditAccPageLoc.last_name_field_loc),\
            'Last name field isn\'t present on this page!'

    def edit_user_name(self):
        first_name_field = self.element_search_and_use(EditAccPageLoc.first_name_field_loc)
        first_name_field.clear()
        first_name_field.send_keys('Abraham')
        last_name_field = self.element_search_and_use(EditAccPageLoc.last_name_field_loc)
        last_name_field.clear()
        last_name_field.send_keys('Warner')
        confirm_password_field = self.element_search_and_use(EditAccPageLoc.confirm_password_field_loc)
        confirm_password_field.send_keys('1111')
        save_button = self.element_search_and_use(EditAccPageLoc.save_button_loc)
        save_button.click()

    def check_applying_changes(self):
        change_message = 'Changes saved successfully.'
        assert self.element_search_and_use(
            EditAccPageLoc.change_message).text == change_message, 'Changes doesn\'t saved!'

    check_changing_user_name = check_changing_user_name

