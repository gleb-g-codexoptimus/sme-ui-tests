from abc import ABC
from typing import Union

from selenium.webdriver.common.by import By

from framework.web.web_element import WebElement
from framework.web.input_element import InputElement
from framework.web.select_element import SelectElement
from framework.web.base_page import BasePage


class RegisterPage(BasePage, ABC):
    UNIQUE_LOC = (By.ID, 'legalForm')
    PHONE_LOC = (By.ID, 'phone')
    LEGAL_FORM_LOC = (By.ID, 'yv_id_1')
    PINFL_LOC = (By.ID, 'pinfl')
    INN_LOC = (By.ID, 'inn')
    COMPANY_NAME_LOC = (By.ID, 'companyName')
    SUBMIT_BTN_LOC = (By.XPATH, '//button[@type="submit"]')
    SMS_LOC = (By.ID, 'code')

    def __init__(self, driver, name):
        super().__init__(driver, name)
        self.unique_element = WebElement(self.driver, self.UNIQUE_LOC, 'Register page -> Unique page element')
        self.phone_field = InputElement(self.driver, self.PHONE_LOC, 'Register page -> Phone field')
        self.legal_form_field = SelectElement(self.driver, self.LEGAL_FORM_LOC, 'Register page -> Legal form field')
        self.pinfl_field = InputElement(self.driver, self.PINFL_LOC, 'Register page -> Pinfl field')
        self.inn_field = InputElement(self.driver, self.INN_LOC, 'Register page -> Inn field')
        self.company_name_field = InputElement(self.driver, self.COMPANY_NAME_LOC, 'Register page -> Company name field')
        self.submit_btn = WebElement(self.driver, self.SUBMIT_BTN_LOC, 'Register page -> Submit button')
        self.sms_field = InputElement(self.driver, self.SMS_LOC, 'Register page -> SMS field')
        self.wait_for_opening(self.unique_element)

    def enter_phone(self, phone):
        self.phone_field.click()
        self.phone_field.send_keys(phone)

    def enter_legal_form(self, index: Union[int, str]):
        self.legal_form_field.click()
        self.legal_form_field.select_by_index(index)

    def enter_pinfl(self, pinfl):
        self.pinfl_field.send_keys(pinfl)

    def enter_inn(self, inn):
        self.pinfl_field.send_keys(inn)

    def enter_company_name(self, company_name):
        self.company_name_field.send_keys(company_name)

    def click_submit_btn(self):
        self.submit_btn.click()

    def enter_otp_code(self):
        self.sms_field.wait_presence()
        console_log = self.driver.get_log()
        code = BasePage.get_otp_code(console_log)
        self.sms_field.send_keys(code)
        self.sms_field.wait_invisibility()
