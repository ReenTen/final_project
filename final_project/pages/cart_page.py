from final_project.pages.base_page import BasePage
from final_project.locators.cart_page_loc import CartPageLoc
from final_project.database_request import check_order_at_db
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import nums_from_string
from decimal import getcontext
from decimal import Decimal as D
import time


class CartPage(BasePage):

    def check_cart_page_url(self):
        cart_page_url = self.chrome.current_url
        assert cart_page_url == CartPageLoc.cart_page_url_loc, 'Error! Cart page URL is not equall recieved link!'

    def check_amount_field(self):
        assert self.element_search_and_use(
            CartPageLoc.amount_field_loc), 'Error! Amount field isn\'t present on this page!'

    def change_amount(self):
        amount_field = self.element_search_and_use(CartPageLoc.amount_field_loc)
        amount_field.clear()
        amount_field.send_keys('3')
        update_button = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(CartPageLoc.update_button_loc))
        update_button.click()
        time.sleep(2)    # Data doesn't refresh after update_button.click()

    def check_price(self, os_unit_cost, duck_price):
        getcontext().prec = 4
        duck_price = '$' + str(D(nums_from_string.get_nums(duck_price)[0]).quantize(D('1.00')))
        assert duck_price == os_unit_cost, f'Error! {duck_price} isn\'t equal {os_unit_cost}!'

    def check_total_price(self, os_unit_cost, os_quantity, os_total_cost):
        getcontext().prec = 4
        total = '$' + str(D(nums_from_string.get_nums(os_unit_cost)[0]).quantize(D('1.00')) * (D(
            nums_from_string.get_nums(os_quantity)[0])))
        assert total == os_total_cost, f"Error! Total price isn\'t equal {os_total_cost}. Price - {total}"

    # Blue duck
    def check_blue_duck_price_at_cart(self):
        os_unit_cost = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_blue_duck_unit_cost_loc)).text
        blue_duck_price = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.blue_duck_price_loc)).text
        self.check_price(os_unit_cost, blue_duck_price)

    def check_blue_duck_os_quantity(self):
        os_quantity = '3'
        blue_duck_quantity = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_blue_duck_quantity_loc)).text
        assert blue_duck_quantity == os_quantity, f'Error! Product quantity isn\'t equal {os_quantity}!'

    def check_blue_duck_total_price(self):
        os_total_cost = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_blue_duck_total_price_loc)).text
        os_unit_cost = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_blue_duck_unit_cost_loc)).text
        os_quantity = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_blue_duck_quantity_loc)).text
        self.check_total_price(os_unit_cost, os_quantity, os_total_cost)

    # Green duck
    def check_green_duck_price_at_cart(self):
        os_unit_cost = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_green_duck_unit_cost_loc)).text
        green_duck_price = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.green_duck_price_loc)).text
        self.check_price(os_unit_cost, green_duck_price)

    def check_green_duck_total_price(self):
        os_total_cost = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_green_duck_total_price_loc)).text
        os_unit_cost = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_green_duck_unit_cost_loc)).text
        os_quantity = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_green_duck_quantity_loc)).text
        self.check_total_price(os_quantity, os_unit_cost, os_total_cost)

    # Purple duck
    def check_purple_duck_price_at_cart(self):
        os_unit_cost = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_purple_duck_unit_cost_loc)).text
        purple_duck_price = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.purple_duck_price_loc)).text
        self.check_price(os_unit_cost, purple_duck_price)

    def check_purple_duck_total_price(self):
        os_total_cost = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_purple_duck_total_price_loc)).text
        os_unit_cost = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_purple_duck_unit_cost_loc)).text
        os_quantity = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.os_purple_duck_quantity_loc)).text
        self.check_total_price(os_quantity, os_unit_cost, os_total_cost)

    def remove_duck_from_cart(self):
        remove_button = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(CartPageLoc.remove_button_loc))
        remove_button.click()

    def check_remove_message(self):
        remove_message = WebDriverWait(self.chrome, 20).until(
            EC.visibility_of_element_located(CartPageLoc.remove_message_loc))
        assert remove_message.text == 'There are no items in your cart.', \
            'Error! You\'ve got something in your cart!'

    def confirm_order(self):
        confirm_order_button = self.element_search_and_use(CartPageLoc.confirm_order_button)
        confirm_order_button.submit()

    def check_order_successful_message(self):
        order_success_message = self.element_search_and_use(CartPageLoc.order_success_message).text
        assert order_success_message == 'Your order is successfully completed!', 'Error. Check your order!'

    check_confirm_order = check_order_at_db
