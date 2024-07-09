from playwright.sync_api import Page
from elements.base_elements import BaseElements

class AboutElements(BaseElements):

    def __init__(self, page: Page):
        super().__init__(page, self.__class__.__name__)

        self.about_page_description = self.page.locator("xpath=//*[contains(@class, 'text-left')]")

    def get_about_page(self):
        self.logger.info('Get the text of the About page...')
        result = self.about_page_description.inner_text().replace("\n\n", " ").strip()
        self.logger.info("Result text: '%s'", result)
        return result
    