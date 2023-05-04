import os
import xlrd
from conftest import PROJECT_ROOT_PATH


def test_read_xls():
    # TODO оформить в тест, добавить ассерты и использовать универсальный путь
    xls_file_path = os.path.join(PROJECT_ROOT_PATH, 'resources', 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_file_path)
    print(f"Количество листов {book.nsheets}")
    print(f"Имена листов {book.sheet_names()}")
    sheet = book.sheet_by_index(0)
    print(f"Количество столбцов {sheet.ncols}")
    print(f"Количество строк {sheet.nrows}")
    print(f"Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=0, colx=1)}")
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))

    assert book.nsheets == 1
    assert book.sheet_names() == ['Sheet1']
    assert sheet.ncols == 8
