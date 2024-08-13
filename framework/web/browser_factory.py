from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config import REMOTE_SERVER_URL


class BrowserFactory:
    @staticmethod
    def get_driver(request):
        service = Service(ChromeDriverManager().install())
        headless = request.config.getoption("--headless")
        options = Options()
        options.add_argument("--enable-logging")
        options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

        if headless:
            options.add_argument("--headless")

        return webdriver.Chrome(service=service, options=options)

    @staticmethod
    def get_remote_driver():
        return webdriver.Remote(command_executor=REMOTE_SERVER_URL)
