import pytest

from framework.web.browser import Browser


# ------------------------------------------------------------------
# Parsing command line arguments
# ------------------------------------------------------------------
def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stage', help='Environment selection, "stage" for example')
    parser.addoption('--locale', action='store', default='ru', help='Localization selection, "ru" for example')
    parser.addoption(
        '--headless',
        dest='headless',
        action='store_const',
        const=bool,
        default=False,
        help='Start browser in headless mode'
    )


# ------------------------------------------------------------------
# Main fixtures
# ------------------------------------------------------------------
@pytest.fixture(scope='function')
def browser(request):
    driver = Browser(request)
    yield driver
    driver.quit()
