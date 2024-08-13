from selenium.webdriver.common.by import By
from framework.web.base_element import BaseElement
from framework.web.web_element import WebElement
from framework.utils.logger import Logger
from typing import Union


class SelectElement(BaseElement):
    def select_by_index(self, index: Union[int, str]):
        Logger.info(f'Selecting: {self.description}, {self.locator}')
        index_loc = (By.ID, f'{self.locator[1]}_{str(index)}')
        index_element = WebElement(self.driver, index_loc, 'Element from select list')
        index_element.click()
