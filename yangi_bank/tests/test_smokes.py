import time

from yangi_bank.actors.user import User
from framework.utils.faker_generator import generate_phone_number, generate_company_name
from framework.utils.pinfl_generator import generate_random_pin_fl
from config import AUTH_LINK, ONBOARDING_LINK


class TestSmokes:

    def test_registration(self, browser):
        browser.get(AUTH_LINK)
        user = User(browser, 'First user')
        user.register(generate_phone_number('76', 9),
                      1,
                      generate_random_pin_fl(),
                      generate_company_name())
        time.sleep(100)
        assert browser.get_current_url() == f'https://{ONBOARDING_LINK}'
