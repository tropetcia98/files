import os.path

import requests
from selene import browser, query
from selenium import webdriver

from tests.script_os import TMP_DIR


def test_text_in_downloaded_file():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver

    browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
    # Вариант скачивания с помощью нажатия по кнопке
    # browser.element('[data-testid="download-raw-button"]').click()
    # time.sleep(5)

    # Вариант скачивания с помощью вшитой ссылки на сайте с аттрибутом href
    download_url = browser.element('[data-testid="raw-button"]').get(query.attribute('href'))
    print(download_url)
    content = requests.get(url=download_url).content
    with open(os.path.join(TMP_DIR, "readme2.rst"), "wb") as file:
        file.write(content)

    with open(r"tmp/readme2.rst") as file:
        file_content_str = file.read()
        assert "test_answer" in file_content_str
