from framework.web.base_element import BaseElement
from framework.utils.logger import Logger


class InputElement(BaseElement):
    def send_keys(self, keys):
        Logger.info(f'Sending keys to input: {keys}')
        element = self.wait_visibility()
        element.send_keys(keys)
        Logger.info('The keys was sent')

    def clear(self):
        Logger.info(f'Clearing input: {self.description}')
        element = self.wait_visibility()
        element.clear()
        Logger.info('The field was cleared')
