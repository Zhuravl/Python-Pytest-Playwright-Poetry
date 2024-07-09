import logging
from playwright.sync_api import BrowserContext, Page
from actions.about_actions import AboutActions

class BaseTest:
    
    def __init__(self, context: BrowserContext, page: Page, name: str):
        self.context = context
        self.page = page
        self.logger = logging.getLogger(name)

        self.about_actions: AboutActions = None
        
    def about_actions(self):
        'Creates and returns AboutActions instance'
        if self.about_actions == None or self.about_actions.context != self.context:
            self.about_actions = AboutActions(self.context, self.page)
        return self.about_actions