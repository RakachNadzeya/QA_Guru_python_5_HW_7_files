import csv
import os.path
from conftest import PROJECT_ROOT_PATH


def test_csv_file_was_properly_zipped():
    # TODO оформить в тест, добавить ассерты и использовать универсальный путь
    csv_file_path = os.path.join(PROJECT_ROOT_PATH, 'resources', 'eggs.csv')

    with open(csv_file_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

        rows = list(csvreader)

        expected_rows = [['Anna', 'Pavel', 'Peter'], ['Alex', 'Serj', 'Yana']]

        for i in rows:
            assert row == expected_rows
