from abc import ABC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.utils.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains


class BaseElement(ABC):
    def __init__(self, driver, locator, description='', timeout=10):
        self.driver = driver
        self.locator = locator
        self.description = description
        self.timeout = timeout

    def wait_presence(self):
        Logger.info(f'Waiting for presence of element: {self.description}')
        element = WebDriverWait(self.driver.get_driver(), self.timeout).until(
            EC.presence_of_element_located(self.locator)
        )
        Logger.info('The element was present')
        return element

    def wait_clickable(self):
        Logger.info(f'Waiting for clickable of element: {self.description}')
        element = WebDriverWait(self.driver.get_driver(), self.timeout).until(
            EC.element_to_be_clickable(self.locator)
        )
        Logger.info('The element was clickable')
        return element

    def wait_invisibility(self):
        Logger.info(f'Waiting for invisibility of element: {self.description}')
        element = WebDriverWait(self.driver.get_driver(), self.timeout).until(
            EC.invisibility_of_element_located(self.locator)
        )
        Logger.info('The element was invisible')
        return element

    def wait_visibility(self):
        Logger.info(f'Waiting for visibility of element: {self.description}')
        element = WebDriverWait(self.driver.get_driver(), self.timeout).until(
            EC.visibility_of_element_located(self.locator)
        )
        Logger.info('The element was visible')
        return element

    # Flows

    def click(self):
        Logger.info(f'Clicking on element: {self.description}')
        self.wait_clickable().click()

    def get_text(self):
        Logger.info(f'Getting text from element: {self.description}')
        element_text = self.wait_presence().text
        Logger.info(f'The text was successfully received {element_text}')
        return element_text

    def get_attribute(self, attribute_name):
        Logger.info(f'Getting attribute from element: {self.description}')
        element_attribute = self.wait_presence().get_attribute(attribute_name)
        Logger.info(f'The attribute value was successfully received {element_attribute}')
        return element_attribute

    def check_is_enabled(self):
        Logger.info(f'Checking if checkbox is enabled: {self.description}')
        element = self.wait_presence().is_enabled()
        Logger.info('The element was checked')
        return element

    # Action Chains
    def drag_and_drop(self, target):
        Logger.info(f'Dragging and dropping from {self} to {target}')
        source = self.wait_clickable()
        target = WebDriverWait(target.driver, target.timeout).until(
            EC.element_to_be_clickable(target.locator)
        )
        ActionChains(self.driver.get_driver()).drag_and_drop(source, target).perform()
        Logger.info('The element was dropped')
        return self

    def double_click(self):
        Logger.info(f'Double clicking on element: {self.locator}')
        element = self.wait_clickable()
        ActionChains(self.driver.get_driver()).double_click(element).perform()
        return self

    def move_cursor_to_element_and_click(self):
        Logger.info(f'Moving cursor on element and click: {self.locator}')
        element = self.wait_clickable()
        ActionChains(self.driver.get_driver()).move_to_element(element).click(element).perform()
        return self

    def move_cursor_to_element(self):
        Logger.info(f'Moving cursor on element: {self.locator}')
        element = self.wait_clickable()
        ActionChains(self.driver.get_driver()).move_to_element(element).perform()
        Logger.info('The cursor was moved')
        return self

    def right_context_click(self):
        Logger.info(f'Right-clicking on element: {self.locator}')
        element = self.wait_visibility()
        ActionChains(self.driver.get_driver()).context_click(element).perform()
        return self

    def click_and_use_key(self, keys, times=1):
        Logger.info(f'Clicking on element and using key: {self.locator}')
        element = self.wait_clickable()
        ActionChains(self.driver.get_driver()).click_and_hold(element).send_keys(
            keys * times
        ).perform()
        return self

    def send_keys_chain(self, keys: str):
        Logger.info(f'Sending keys: {keys}')
        self.wait_clickable()
        ActionChains(self.driver.get_driver()).click().send_keys(keys).perform()
        return self
