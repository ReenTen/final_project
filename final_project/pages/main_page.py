from final_project.pages.base_page import BasePage
from final_project.locators.main_page_loc import MainPageLoc


class MainPage(BasePage):

    def check_main_page_url(self):
        main_page_url = self.chrome.current_url
        assert main_page_url == MainPageLoc.main_page_url_loc, 'Error! Main page URL is not equall recieved link!'

    def check_change_regional_settings_button(self):
        assert self.element_search_and_use(
            MainPageLoc.change_button_loc), 'Error! Change button isn\'t present on this page!'

    def open_regional_settings(self):
        change_button = self.element_search_and_use(MainPageLoc.change_button_loc)
        change_button.click()

    def change_regional_settings(self):
        rs_currency_field = self.element_search_and_use(MainPageLoc.rs_currency_field_loc)
        rs_currency_field.click()
        rs_currency_eur = self.element_search_and_use(MainPageLoc.rs_currency_eur_loc)
        rs_currency_eur.click()

        rs_country_field = self.element_search_and_use(MainPageLoc.rs_country_field_loc)
        rs_country_field.click()
        rs_country_china = self.element_search_and_use(MainPageLoc.rs_country_zimbabwe_loc)
        rs_country_china.click()
        rs_save_button = self.element_search_and_use(MainPageLoc.rs_save_button_loc)
        rs_save_button.click()

    def check_change_currency(self):
        current_currency = 'EUR'
        assert self.element_search_and_use(
            MainPageLoc.current_currency_loc).text == current_currency, 'Error! Currency unit isn\'t change!'

    def check_change_country(self):
        current_country = 'Zimbabwe'
        assert self.element_search_and_use(
            MainPageLoc.current_country_loc).text == current_country, 'Error! Country isn\'t change!'

    def check_email_address_field(self):
        assert self.element_search_and_use(
            MainPageLoc.email_address_field_loc), 'Error! E-mail address field isn\'t present on this page!'

    def check_password_field(self):
        assert self.element_search_and_use(
            MainPageLoc.password_field_loc), 'Error! Password field isn\'t present on this page!'

    def check_remember_me_checkbox(self):
        assert self.element_search_and_use(
            MainPageLoc.remember_me_checkbox_loc), 'Error! "Remember me" checkbox isn\'t present on this page!'

    def check_login_button(self):
        assert self.element_search_and_use(
            MainPageLoc.login_button_loc), 'Error! Login button isn\'t present on this page!'

    def login_customer(self):
        email_address_field = self.element_search_and_use(MainPageLoc.email_address_field_loc)
        email_address_field.send_keys('abcd@google.com')
        password_field = self.element_search_and_use(MainPageLoc.password_field_loc)
        password_field.send_keys('1111')
        remember_me_checkbox = self.element_search_and_use(MainPageLoc.remember_me_checkbox_loc)
        remember_me_checkbox.click()
        login_button = self.element_search_and_use(MainPageLoc.login_button_loc)
        login_button.click()

    def check_login_customer(self):
        assert self.element_search_and_use(
            MainPageLoc.customer_logged_in_loc), 'Authorisation error! Please, check your data!'

    def check_blue_duck_at_store(self):
        assert self.element_search_and_use(MainPageLoc.blue_duck_loc), 'Error! Blue Duck isn\'t sale in this store!'

    def check_green_duck_at_store(self):
        assert self.element_search_and_use(MainPageLoc.green_duck_loc), 'Error! Green Duck isn\'t sale in this store!'

    def check_purple_duck_at_store(self):
        assert self.element_search_and_use(MainPageLoc.purple_duck_loc), 'Error! Purple Duck isn\'t sale in this store!'

    def check_cart_button(self):
        assert self.element_search_and_use(MainPageLoc.cart_loc), 'Error! Cart button isn\'t present on this page!'

    def open_blue_duck_page(self):
        blue_duck = self.element_search_and_use(MainPageLoc.blue_duck_loc)
        blue_duck.click()

    def open_green_duck_page(self):
        green_duck = self.element_search_and_use(MainPageLoc.green_duck_loc)
        green_duck.click()

    def open_purple_duck_page(self):
        purple_duck = self.element_search_and_use(MainPageLoc.purple_duck_loc)
        purple_duck.click()

    def check_duck_at_cart(self):
        cart_is_empty = self.element_search_and_use(MainPageLoc.quantity_of_goods_at_cart_loc).text
        assert cart_is_empty != '0', f'Error! Cart is empty!'

    def open_cart_page(self):
        cart_button = self.element_search_and_use(MainPageLoc.cart_loc)
        cart_button.click()

    def check_edit_account_link(self):
        assert self.element_search_and_use(MainPageLoc.edit_account_link_loc), \
            'Error! Edit account link doesn\'t present on this page!'

    def open_edit_account_page(self):
        edit_account_link = self.element_search_and_use(MainPageLoc.edit_account_link_loc)
        edit_account_link.click()
