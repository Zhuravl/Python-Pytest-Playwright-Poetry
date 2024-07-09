import pytest
from tests.base_test import BaseTest
from core.enums.pages_enum import Pages

from core.enums.language_enum import Language

class TestSignUp(BaseTest):

    def __init__(self, get_context, get_browser):
        super().__init__(get_context, get_browser, self.__class__.__name__)

    def test_sign_up_page_navigation(self):
        target_page = Pages.SIGN_UP

        self.about_actions().open_web_site()
        self.about_actions().navigate_to(target_page)
        #Verify that the user can navigate to the Sign Up page
        assert self.about_actions().is_on_page(target_page)