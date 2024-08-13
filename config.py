import os

REMOTE_SERVER_URL = 'https://{url}:{port}/wd/hub'
SCREENSHOT_PATH = os.getcwd()
TEST_FILES_PATH = f'{os.getcwd()}\\yangi_bank\\tests\\test_files'


BASE_LINK = 'sme-stg.yangi.uz'
AUTH_LINK = f'{BASE_LINK}/session/new'
REGISTER_LINK = f'{BASE_LINK}/session/registration'
ONBOARDING_LINK = f'{BASE_LINK}/welcome'
