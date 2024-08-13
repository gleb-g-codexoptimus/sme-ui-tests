import re
import time

from framework.utils.logger import Logger
from framework.utils.utils_etc import parse_log_values
from config import BASE_LINK


class BasePage:
    def __init__(self, driver, name=''):
        self.driver = driver
        self.name = name

    def wait_for_opening(self, element):
        Logger.info(f'Waiting for opening of page: {self.name}')
        element.wait_presence()
        Logger.info('Page was opened')

    @staticmethod
    def get_otp_code(console_log):
        Logger.info(f'Getting otp code from browser console')
        code_list = parse_log_values(console_log, 'message', BASE_LINK)
        # Using regular expression for search codes
        sms_code = re.search(r'"(\d+)"$', *code_list)
        Logger.info(f'Successfully received the code: {sms_code.group()}')
        return sms_code.group()
