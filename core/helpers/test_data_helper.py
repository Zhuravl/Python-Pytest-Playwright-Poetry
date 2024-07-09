import random
from datetime import datetime, timezone
from core.consts.date_format_const import DateFormat

class TestDataHelper:

    _LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _NON_ZERO_DIGITS = "123456789"
    _WITH_ZERO_DIGITS = "0" + _NON_ZERO_DIGITS
    _SPECIALS = "/*-+.,~!@#$%^&()_="
    _ALL_CHARACTERS = _LETTERS + _LETTERS.lower() + _WITH_ZERO_DIGITS
    _ALL_CHARACTERS_INCLUDE_SPECIALS = _ALL_CHARACTERS + _SPECIALS
    
    @staticmethod
    def get_random_string(symbols, length):
        'Returns a string of randomly choiced symbols with the defined lenght'
        result = ''.join(random.choice(symbols) for _ in range(length))
        return result
    
    @classmethod
    def get_random_email(cls):
        'Returns a randomly generated email'
        result = f"{cls.get_random_string(cls._LETTERS, 10)}@{cls.get_random_string(cls._LETTERS, 5)}.{cls.get_random_string(cls._LETTERS, 3)}"
        return result.lower()
    
    @classmethod
    def get_random_password(cls):
        'Returns a randomly generated password'
        result = f"{cls.get_random_string(cls._LETTERS, 3)}{cls.get_random_string(cls._WITH_ZERO_DIGITS, 3)}{cls.get_random_string(cls._SPECIALS, 3)}{cls.get_random_string(cls._LETTERS.lower(), 3)}"
        return result
    
    @classmethod
    def get_random_name(cls):
        'Returns a randomly generated name'
        return cls.get_random_string(cls._ALL_CHARACTERS, 16)
    
    @classmethod
    def get_random_number(cls, lenght):
        'Returns randomly generated number with the defined length'
        if lenght < 1:
            raise ValueError("Length must be at least 1!")
        result = f"{cls.get_random_string(cls._NON_ZERO_DIGITS, 1)}{cls.get_random_string(cls._WITH_ZERO_DIGITS, lenght - 1)}"
        return int(result)

    @staticmethod
    def get_timestamp():
        'Returns the timestamp'
        return datetime.now(timezone.utc).strftime(DateFormat.YYYYMMDDHHMMSS)
    