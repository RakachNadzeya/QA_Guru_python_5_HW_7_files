import os
import time

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from conftest import DOWNLOADED_FILE_PATH


def test_download_file_using_browser():
    # TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp
    DOWNLOADED_FILE = os.path.join(DOWNLOADED_FILE_PATH, 'pytest-main.zip')
    if not os.path.exists(DOWNLOADED_FILE_PATH):
        os.mkdir(DOWNLOADED_FILE_PATH)

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": DOWNLOADED_FILE_PATH,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)

    size = os.path.getsize(DOWNLOADED_FILE)
    print(size)
    assert size == 1565002
    os.remove(DOWNLOADED_FILE)
