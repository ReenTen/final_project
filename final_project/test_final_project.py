from final_project.pages.main_page import MainPage
from final_project.pages.cart_page import CartPage
from final_project.pages.blue_duck_page import BlueDuckPage
from final_project.pages.green_duck_page import GreenDuckPage
from final_project.pages.purple_duck_page import PurpleDuckPage
from final_project.pages.edit_acc_page import EditAccPage
import allure


link = 'http://localhost/litecart/en/'


@allure.feature('Testing Litecart store')
class TestLitecartStore:
    @allure.story('Guest can change regional settings like country and currency')
    def test_guest_can_change_regional_settings(self, open_browser):
        main_page = MainPage(open_browser, link)
        with allure.step('Opening main page'):
            main_page.open_page()
        with allure.step('Checking main page url'):
            main_page.check_main_page_url()
        with allure.step('Checking regional settings window'):
            main_page.check_change_regional_settings_button()
        with allure.step('Open regional settings window'):
            main_page.open_regional_settings()
        with allure.step('Changing regional settings like country and currency'):
            main_page.change_regional_settings()
        with allure.step('Checking changing currency at regional settings'):
            main_page.check_change_currency()
        with allure.step('Checking changing country at regional settings'):
            main_page.check_change_country()

    @allure.story('Guest can login and add three different add duck to cart')
    def test_guest_can_login_and_add_duck_to_cart(self, open_browser):
        main_page = MainPage(open_browser, link)
        with allure.step('Opening main page'):
            main_page.open_page()
        with allure.step('Checking main page url'):
            main_page.check_main_page_url()
        with allure.step('Checking e-mail address field'):
            main_page.check_email_address_field()
        with allure.step('Checking password address field'):
            main_page.check_password_field()
        with allure.step('Checking "remember me" checkbox'):
            main_page.check_remember_me_checkbox()
        with allure.step('Checking login button'):
            main_page.check_login_button()
        with allure.step('Login as abcd@google.com user'):
            main_page.login_customer()
        with allure.step('Checking login user'):
            main_page.check_login_customer()
        with allure.step('Checking blue duck at store'):
            main_page.check_blue_duck_at_store()
        with allure.step('Checking green duck at store'):
            main_page.check_green_duck_at_store()
        with allure.step('Checking purple duck at store'):
            main_page.check_purple_duck_at_store()

        with allure.step('Opening purple duck page from main page'):
            main_page.open_purple_duck_page()
            purple_duck_page = PurpleDuckPage(open_browser, url=open_browser.current_url)
        with allure.step('Checking purple duck page url'):
            purple_duck_page.check_purple_duck_page_url()
        with allure.step('Checking "Add to cart" button at "purple duck" page'):
            purple_duck_page.check_purple_duck_add_to_cart_button()
        with allure.step('Add duck to cart at "purple duck" page'):
            purple_duck_page.add_purple_duck_to_cart()

        with allure.step('Opening green duck page from purple duck page'):
            purple_duck_page.open_green_duck_page()
            green_duck_page = GreenDuckPage(open_browser, url=open_browser.current_url)
        with allure.step('Checking green duck page url'):
            green_duck_page.check_green_duck_page_url()
        with allure.step('Checking "Add to cart" button at "green duck" page'):
            green_duck_page.check_green_duck_add_to_cart_button()
        with allure.step('Add duck to cart at "green duck" page'):
            green_duck_page.add_green_duck_to_cart()

        with allure.step('Opening blue duck page from green page'):
            green_duck_page.open_blue_duck_page()
            blue_duck_page = BlueDuckPage(open_browser, url=open_browser.current_url)
        with allure.step('Checking blue duck page url'):
            blue_duck_page.check_blue_duck_page_url()
        with allure.step('Checking "Add to cart" button at "blue duck" page'):
            blue_duck_page.check_add_to_cart_button()
        with allure.step('Add duck to cart at "blue duck" page'):
            blue_duck_page.add_duck_to_cart()

        with allure.step('Checking, that cart has goods'):
            main_page.check_duck_at_cart()
        with allure.step('Opening cart page from "blue duck" page'):
            blue_duck_page.open_cart_page()
            cart_page = CartPage(open_browser, url=open_browser.current_url)

        with allure.step('Checking cart page url'):
            cart_page.check_cart_page_url()

        with allure.step('Checking, that blue duck price at cart equall blue duck price at order table'):
            cart_page.check_blue_duck_price_at_cart()
        with allure.step('Checking blue duck total price at order table'):
            cart_page.check_blue_duck_total_price()

        with allure.step('Checking, that green duck price at cart equall green duck price at order table'):
            cart_page.check_green_duck_price_at_cart()
        with allure.step('Checking green duck total price at order table'):
            cart_page.check_green_duck_total_price()

        with allure.step('Checking, that purple duck price at cart equall green duck price at order table'):
            cart_page.check_purple_duck_price_at_cart()
        with allure.step('Checking purple duck total price at order table'):
            cart_page.check_purple_duck_total_price()

        with allure.step('Confirming order'):
            cart_page.confirm_order()
        with allure.step('Checking order successful message'):
            cart_page.check_order_successful_message()
        with allure.step('Checking order at database'):
            cart_page.check_confirm_order()

    @allure.story('Guest can login and change his name')
    def test_guest_can_login_and_change_his_name(self, open_browser):
        main_page = MainPage(open_browser, link)
        with allure.step('Opening main page'):
            main_page.open_page()
        with allure.step('Checking main page url'):
            main_page.check_main_page_url()
        with allure.step('Checking e-mail address field'):
            main_page.check_email_address_field()
        with allure.step('Checking password address field'):
            main_page.check_password_field()
        with allure.step('Checking "remember me" checkbox'):
            main_page.check_remember_me_checkbox()
        with allure.step('Checking login button'):
            main_page.check_login_button()
        with allure.step('Login as abcd@google.com user'):
            main_page.login_customer()
        with allure.step('Checking login user'):
            main_page.check_login_customer()

        with allure.step('Opening edit acc page'):
            main_page.open_edit_account_page()
            edit_acc_page = EditAccPage(open_browser, url='http://localhost/litecart/en/edit_account')
        with allure.step('Checking edit acc page url'):
            edit_acc_page.check_edit_account_page_url()
        with allure.step('Checking first name field'):
            edit_acc_page.check_first_name_field()
        with allure.step('Checking last name field'):
            edit_acc_page.check_last_name_field()
        with allure.step('Changing users first and last name'):
            edit_acc_page.edit_user_name()
        with allure.step('Checking changing users first and last name at database'):
            edit_acc_page.check_changing_user_name()

    @allure.story('Guest can add duck to cart and remove it')
    def test_guest_can_add_duck_to_cart_and_remove_it(self, open_browser):
        main_page = MainPage(open_browser, link)
        with allure.step('Opening main page'):
            main_page.open_page()
        with allure.step('Checking main page url'):
            main_page.check_main_page_url()
        with allure.step('Opening "blue duck" page'):
            main_page.open_blue_duck_page()
            blue_duck_page = BlueDuckPage(open_browser, url=open_browser.current_url)
        with allure.step('Checking "blue duck" page url'):
            blue_duck_page.check_blue_duck_page_url()
        with allure.step('Checking "Add to cart" button at "blue duck" page'):
            blue_duck_page.check_add_to_cart_button()
        with allure.step('Add duck to cart at "blue duck" page'):
            blue_duck_page.add_duck_to_cart()
        with allure.step('Opening cart page'):
            blue_duck_page.open_cart_page()
            cart_page = CartPage(open_browser, url=open_browser.current_url)
        with allure.step('Checking cart page url'):
            cart_page.check_cart_page_url()
        with allure.step('Checking amount field'):
            cart_page.check_amount_field()
        with allure.step('Change amount blue duck'):
            cart_page.change_amount()
        with allure.step('Checking blue duck price at order summary'):
            cart_page.check_blue_duck_price_at_cart()
        with allure.step('Checking amount blue duck at order summary'):
            cart_page.check_blue_duck_os_quantity()
        with allure.step('Checking blue duck total price at order summary'):
            cart_page.check_blue_duck_total_price()
        with allure.step('Remove blue duck from cart'):
            cart_page.remove_duck_from_cart()
        with allure.step('Checking, that blue duck remove from cart by remove message'):
            cart_page.check_remove_message()
