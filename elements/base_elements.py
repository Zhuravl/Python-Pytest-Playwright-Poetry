import logging
from playwright.sync_api import Page
from core.enums.language_enum import Language

class BaseElements:

    def __init__(self, page: Page, name: str = 'BaseElements'):
        self.page = page
        self.logger = logging.getLogger(name)
        self.language_selector = self.page.locator("xpath=//*[contains(@class, 'navbar-nav')]//select")
        self.about_link = self.page.locator("xpath=//a[@href='/about']")
        self.login_link = self.page.locator("xpath=//a[@href='/login']")
        self.register_link = self.page.locator("xpath=//a[@href='/register']")

    def select_language(self, lng: Language):
        self.logger.info("Selecting the language option - '%s'", lng)
        self.language_selector.select_option(lng.value)

    def click_about_link(self):
        self.logger.info("Clicking the About link")
        self.about_link.click

    def click_login_link(self):
        self.logger.info("Clicking the Sign In link")
        self.login_link.click

    def click_register_link(self):
        self.logger.info("Clicking the Sign Up link")
        self.register_link.click