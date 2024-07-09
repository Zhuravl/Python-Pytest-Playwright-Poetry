from playwright.sync_api import BrowserContext, Page
from actions.base_actions import BaseActions
from elements.about_elements import AboutElements

class AboutActions(BaseActions):

    def __init__(self, context: BrowserContext, page: Page):
        super().__init__(context, page, self.__class__.__name__)
        self.about_elements = AboutElements(self.page)

    def get_about_page(self):
        self.logger.info('Get the text of the About page...')
        result = self.about_elements.get_about_page()
        self.logger.info("Result text: '%s'", result)
        return result