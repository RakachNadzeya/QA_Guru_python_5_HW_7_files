import os
from pypdf import PdfReader
from conftest import PROJECT_ROOT_PATH


def test_read_pdf():
    # TODO оформить в тест, добавить ассерты и использовать универсальный путь
    pdf_file_path = os.path.join(PROJECT_ROOT_PATH, 'resources', 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(pdf_file_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert number_of_pages == 412
