from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, browser, url):
        self.chrome = browser
        self.url = url
        self.chrome.implicitly_wait(5)
        self.chrome.maximize_window()

    def open_page(self):
        self.chrome.get(self.url)

    def element_search_and_use(self, locator):
        try:
            element = self.chrome.find_element(*locator)
        except NoSuchElementException:
            return 'Element is not present on this page!'
        return element
