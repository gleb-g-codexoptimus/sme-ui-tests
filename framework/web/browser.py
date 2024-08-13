import json

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.web.browser_factory import BrowserFactory
from framework.utils.faker_generator import generate_text
from framework.web.base_element import BaseElement
from framework.utils.logger import Logger

from config import SCREENSHOT_PATH, TEST_FILES_PATH


class Browser:
    def __init__(self, request, remote=False):
        self._driver = (
            BrowserFactory.get_remote_driver() if remote else BrowserFactory.get_driver(request)
        )

    def get_driver(self):
        return self._driver

    def get(self, link, protocol='https://', username=False, password=False):
        Logger.info(f'Going to {link}')
        self._driver.get(
            f'{protocol}{username}:{password}@{link}'
        ) if username and password else self._driver.get(f'{protocol}{link}')

    def get_log(self):
        Logger.info(f'Getting logs from browser console')
        logs = self._driver.get_log("browser")
        Logger.info(f'Received logs: {logs}')
        return logs

    def refresh(self):
        Logger.info('Refreshing browser')
        self._driver.refresh()
        Logger.info('Tab refreshed')

    def back(self):
        Logger.info('Back to prev tab')
        self._driver.back()
        Logger.info('Prev tab opened')

    def close(self):
        Logger.info('Closing tab')
        self._driver.close()
        Logger.info('Tab was closed.')

    def close_other_tabs(self, original_window):
        Logger.info('Closing other tabs')
        all_windows = self.get_window_handles()
        for window in all_windows:
            if window != original_window:
                self.switch_to_window(window)
                self.close()
        Logger.info('Successfully closed.')

    def quit(self):
        Logger.info('Quitting browser')
        self._driver.quit()
        Logger.info('Browser was closed.')

    def get_current_url(self):
        Logger.info('Getting current url')
        url = self._driver.current_url
        Logger.info('Url received')
        return url

    def get_page_source(self):
        Logger.info('Getting page source')
        source = self._driver.page_source
        Logger.info('Source received')
        return source

    def switch_to_window(self, window_name):
        Logger.info(f'Switching to window: {window_name}')
        self._driver.switch_to.window(window_name)
        Logger.info('Switched to window')

    def switch_to_iframe(self, frame_element: BaseElement, timeout=10):
        Logger.info(f'Switching to frame: {frame_element.description}')
        WebDriverWait(self._driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it(frame_element.locator)
        )
        Logger.info('Switched to iframe')

    def switch_to_default_context(self):
        Logger.info('Switching to default context')
        self._driver.switch_to.default_content()
        Logger.info('Switched to default context')

    def get_current_window_handle(self):
        Logger.info('Getting current window')
        curr_win = self._driver.current_window_handle
        Logger.info('Current window received')
        return curr_win

    def get_window_handles(self):
        Logger.info('Getting window handles')
        win = self._driver.window_handles
        Logger.info('Window received')
        return win

    def get_cookie(self, name):
        Logger.info(f'Getting cookie: {name}')
        cookie = self._driver.get_cookie(name)
        Logger.info('Cookies received')
        return cookie

    def take_screenshot(self):
        Logger.info('Taking screenshot of page')
        self._driver.save_screenshot(SCREENSHOT_PATH)
        Logger.info('Screenshot saved')

    def execute_script(self, script, *args):
        Logger.info('Executing script')
        self._driver.execute_script(script, *args)
        Logger.info('Script completed successfully')

    # Alert methods

    def switch_to_alert(self, timeout=10):
        Logger.info('Switching to alert')
        WebDriverWait(self._driver, timeout).until(EC.alert_is_present())
        switch_alert = self._driver.switch_to.alert
        Logger.info('Alert switched')
        return switch_alert

    def accept_alert(self):
        Logger.info('Accepting alert')
        alert = self.switch_to_alert()
        alert.accept()
        Logger.info('Alert accepted')

    def dismiss_alert(self):
        Logger.info('Cancelling alert')
        alert = self.switch_to_alert()
        alert.dismiss()
        Logger.info('Alert dismissed')

    def write_text_and_confirm(self, text):
        Logger.info(f'Writing text to alert and confirming: {text}')
        alert = self.switch_to_alert()
        alert.send_keys(text)
        alert.accept()
        Logger.info('Alert accepted')

    def get_alert_text(self):
        Logger.info('Getting text from alert')
        alert = self.switch_to_alert()
        Logger.info('Alert switched')
        return alert.text

    def check_js_alert(self):
        Logger.info('Checking js alert')
        self._driver.execute_script('jsAlert()')
        self.accept_alert()
        Logger.info('Alert checked')

    def check_js_confirm(self):
        Logger.info('Checking js confirm')
        self._driver.execute_script('jsConfirm()')
        self.accept_alert()
        Logger.info('Alert confirmed')

    def check_js_prompt(self):
        Logger.info('Checking js prompt')
        self._driver.execute_script('jsPrompt()')
        rand_text = generate_text(60)
        self.write_text_and_confirm(rand_text)
        Logger.info('Alert confirmed')
        return rand_text
