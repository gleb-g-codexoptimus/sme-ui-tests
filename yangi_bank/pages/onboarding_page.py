from abc import ABC

from selenium.webdriver.common.by import By

from framework.web.web_element import WebElement
from framework.web.input_element import InputElement
from framework.web.base_page import BasePage


class OnboardingPage(BasePage, ABC):
    UNIQUE_LOC = (By.XPATH, '//div[@class="vc-chat-bodyy"]')
    MESSAGE_LOC = (By.XPATH, '//div[@class="vc-message-form-textarea"]')
    FILE_BTN = (By.XPATH, '//div[@class="vc-message-form-fileinput-wrapper"]')
    MSG_SUBMIT_BTN_LOC = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, driver, name):
        super().__init__(driver, name)
        self.unique_element = WebElement(self.driver, self.UNIQUE_LOC, 'Onboarding page -> Unique page element')
        self.message_field = InputElement(self.driver, self.MESSAGE_LOC, 'Onboarding page -> Message field')
        self.attach_file_btn = WebElement(self.driver, self.FILE_BTN, 'Onboarding page -> Attachment btn')
        self.submit_msg_btn = WebElement(self.driver, self.MSG_SUBMIT_BTN_LOC, 'Onboarding page -> Submit btn')
        self.wait_for_opening(self.unique_element)
