import pytest
from tests.base_test import BaseTest
from core.enums.pages_enum import Pages

from core.enums.language_enum import Language

class TestAbout(BaseTest):

    def __init__(self, get_context, get_browser):
        super().__init__(get_context, get_browser, self.__class__.__name__)

    def test_about_page_navigation(self):
        target_page = Pages.ABOUT

        self.about_actions().open_web_site()
        self.about_actions().navigate_to(target_page)
        #Verify that the user can navigate to the About page
        assert self.about_actions().is_on_page(target_page)