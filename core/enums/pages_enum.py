from enum import Enum

class Pages(Enum):
    ABOUT = {'name': 'About', 'value': 'about'}
    SIGN_IN = {'name': 'Sign In', 'value': 'login'}
    SIGN_UP = {'name': 'Sign Up', 'value': 'register'}
    HOME = {'name': 'Home', 'value': ''}