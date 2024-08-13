import os

from yangi_bank.actors.user import User
from config import AUTH_LINK


class TestAuth:
    def test_basic_authorization(self, browser):
        browser.get(AUTH_LINK)
        user = User(browser, 'First user')
        user.login(os.getenv("AUTH_NUMBER"), os.getenv("AUTH_PASSWORD"))
