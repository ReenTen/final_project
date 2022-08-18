from selenium.webdriver.common.by import By


class EditAccPageLoc:

    edit_acc_page_url = 'http://localhost/litecart/en/edit_account'

    first_name_field_loc = (By.XPATH, '//input[@name="firstname"]')
    last_name_field_loc = (By.XPATH, '//input[@name="lastname"]')
    confirm_password_field_loc = (By.XPATH, '//input[@name="confirmed_password"]')
    save_button_loc = (By.XPATH, '//button[@name="save"]')
    change_message = (By.XPATH, '//div[@class="notice_success"]')
