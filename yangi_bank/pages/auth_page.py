import time
from abc import ABC

from selenium.webdriver.common.by import By

from framework.web.web_element import WebElement
from framework.web.input_element import InputElement
from framework.web.base_page import BasePage


class AuthPage(BasePage, ABC):
    UNIQUE_LOC = (By.XPATH, '//*[@id="app"]//main/div/div')
    PHONE_LOC = (By.ID, 'phone')
    SMS_LOC = (By.ID, 'code')
    SUBMIT_BTN_LOC = (By.XPATH, '//button[@type="submit"]')
    PASSWORD_LOC = (By.ID, 'password')
    REGISTER_BTN_LOC = (By.XPATH, '//button[@type="button"]')

    def __init__(self, driver, name):
        super().__init__(driver, name)
        self.unique_element = WebElement(self.driver, self.UNIQUE_LOC, 'Auth page -> Unique page element')
        self.phone_field = InputElement(self.driver, self.PHONE_LOC, 'Auth form -> Phone field')
        self.submit_btn = WebElement(self.driver, self.SUBMIT_BTN_LOC, 'Auth form -> Submit button')
        self.sms_field = InputElement(self.driver, self.SMS_LOC, 'Auth form -> SMS field')
        self.password_field = InputElement(self.driver, self.PASSWORD_LOC, 'Auth form -> Password field')
        self.register_btn = WebElement(self.driver, self.REGISTER_BTN_LOC, 'Auth form -> Register button')
        self.wait_for_opening(self.unique_element)

    def enter_phone(self, phone):
        self.phone_field.send_keys(phone)
        self.submit_btn.click()

    def enter_otp_code(self):
        self.sms_field.wait_presence()
        console_log = self.driver.get_log()
        code = BasePage.get_otp_code(console_log)
        self.sms_field.send_keys(code)
        self.sms_field.wait_invisibility()

    def enter_password(self, password):
        self.password_field.send_keys(password)
        self.submit_btn.click()

    def go_to_register(self):
        self.register_btn.click()
