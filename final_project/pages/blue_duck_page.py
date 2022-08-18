from final_project.pages.base_page import BasePage
from final_project.locators.blue_duck_page_loc import BlueDuckPageLoc
from final_project.pages.main_page import MainPage
import time


class BlueDuckPage(BasePage):

    def check_blue_duck_page_url(self):
        blue_duck_page_url = self.chrome.current_url
        assert blue_duck_page_url == BlueDuckPageLoc.blue_duck_page_url_loc

    def check_add_to_cart_button(self):
        assert self.element_search_and_use(
            BlueDuckPageLoc.add_to_cart_button_loc), '"Add to cart" button isn\'t present on this page!'

    def add_duck_to_cart(self):
        add_to_cart_button = self.element_search_and_use(BlueDuckPageLoc.add_to_cart_button_loc)
        add_to_cart_button.click()
        time.sleep(2)   # Adding duck has animation. Don't add product correct without time.sleep.

    open_cart_page = MainPage.open_cart_page
    open_purple_duck_page = MainPage.open_purple_duck_page
