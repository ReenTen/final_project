from final_project.pages.base_page import BasePage
from final_project.locators.purple_duck_page_loc import PurpleDuckPageLoc
from final_project.pages.blue_duck_page import BlueDuckPage
from final_project.pages.main_page import MainPage


class PurpleDuckPage(BasePage):

    def check_purple_duck_page_url(self):
        purple_duck_page_url = self.chrome.current_url
        assert purple_duck_page_url == PurpleDuckPageLoc.purple_duck_page_url_loc

    open_green_duck_page = MainPage.open_green_duck_page
    check_purple_duck_add_to_cart_button = BlueDuckPage.check_add_to_cart_button
    add_purple_duck_to_cart = BlueDuckPage.add_duck_to_cart

