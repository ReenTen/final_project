from final_project.pages.base_page import BasePage
from final_project.locators.green_duck_page_loc import GreenDuckPageLoc
from final_project.pages import blue_duck_page
from final_project.pages import main_page


class GreenDuckPage(BasePage):

    def check_green_duck_page_url(self):
        yellow_duck_page_url = self.chrome.current_url
        assert yellow_duck_page_url == GreenDuckPageLoc.green_duck_page_url_loc

    check_green_duck_add_to_cart_button = blue_duck_page.BlueDuckPage.check_add_to_cart_button
    add_green_duck_to_cart = blue_duck_page.BlueDuckPage.add_duck_to_cart
    open_blue_duck_page = main_page.MainPage.open_blue_duck_page
