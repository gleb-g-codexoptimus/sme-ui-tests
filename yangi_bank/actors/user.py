import time

from yangi_bank.pages.auth_page import AuthPage
from yangi_bank.pages.register_page import RegisterPage

from typing import Union


class User:
    def __init__(self, driver, name):
        self.driver = driver
        self.name = name

    def login(self, phone, password):
        auth_page = AuthPage(self.driver, 'Page with login form')
        auth_page.enter_phone(phone)
        auth_page.enter_otp_code()
        auth_page.enter_password(password)

    def register(self, phone: str, legal_form_index: Union[int, str], pinfl_or_inn: str, company_name):
        auth_page = AuthPage(self.driver, 'Page with login form')
        auth_page.go_to_register()
        register_page = RegisterPage(self.driver, 'Page with register form')
        register_page.enter_phone(phone)
        register_page.enter_legal_form(legal_form_index)
        register_page.enter_pinfl(pinfl_or_inn) if legal_form_index == 2 else register_page.enter_inn(pinfl_or_inn)
        register_page.enter_company_name(company_name)
        register_page.click_submit_btn()
        register_page.submit_btn.wait_invisibility()
        register_page.enter_otp_code()
