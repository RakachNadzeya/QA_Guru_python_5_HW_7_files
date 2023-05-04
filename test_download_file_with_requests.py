import os.path
import requests
from conftest import DOWNLOADED_FILE_PATH


def test_downloaded_file_size():
    # TODO сохранять и читать из tmp, использовать универсальный путь
    url = "https://selenium.dev/images/selenium_logo_square_green.png"
    if not os.path.exists(DOWNLOADED_FILE_PATH):
        os.mkdir(DOWNLOADED_FILE_PATH)
    downloaded_image = os.path.join(DOWNLOADED_FILE_PATH, 'selenium_logo.png')

    r = requests.get(url)

    with open(downloaded_image, "wb") as file:
        file.write(r.content)

    size = os.path.getsize(downloaded_image)

    assert size == 30803

    os.remove(downloaded_image)
