from playwright.sync_api import BrowserContext, Page
from tests.conftest import get_url
from core.enums.pages_enum import Pages
from core.enums.language_enum import Language
from elements.base_elements import BaseElements
import logging

class BaseActions:

    def __init__(self, context: BrowserContext, page: Page, name: str):
        self.context = context
        self.page = page
        self.logger = logging.getLogger(name)
        self.base_elements = BaseElements(self.page)

    def open_web_site(self):
        'Opens the target Website'
        self.logger.info('Open the web-site')
        self.page.goto(get_url())

    def is_on_page(self, page: Pages):
        'Checks if on the defined page'
        self.logger.info("Checking is on the '%s' page...", page)
        current_url = self.page.url
        if page == Pages.HOME:
            result = current_url == get_url()
        else:
            result = page.value in current_url
        self.logger.info("Is on '%s' page? - %s", page, result)
        return result
    
    def navigate_to(self, page: Pages):
        'Navigates to the defined page if it has not opened yet'
        self.logger.info("Navigate to the page '%s'...", page)
        if not self.is_on_page(page):
            match self.page:
                case Pages.ABOUT:
                    self.base_elements.click_about_link()
                case Pages.SIGN_IN:
                    self.base_elements.click_login_link()
                case Pages.SIGN_UP:
                    self.base_elements.click_register_link()
                case _:
                    raise ValueError(f"Can not recognize the page with name: '{self.page}'!")
        self.logger.info("The navigation has been successfully done!")

    def select_language(self, lng: Language):
        'Sets the defined language'
        self.logger.info("Set the language '%s'...", lng)
        self.base_elements.select_language(lng)
        self.logger.info("The language has been successfully set!")
