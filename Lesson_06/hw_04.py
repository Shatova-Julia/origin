# Прочитать сохранённый json-файл и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец
# и добавив новый столбец “телефон”.

import csv

b_dict = {
          '159612': ('Tom', 23, 5554378),
          '310640': ('Noah', 32, 5558732),
          '044208': ('Jacob', 41, 5559065),
          '233648': ('Liam', 21, 5552314),
          '053872': ('Michael', 27, 5550956),
          '403600': ('Anderson', 54, 5552343)
}

with open('name_two.json', 'r') as f:
    with open('name_three.csv', 'w', encoding='UTF-8') as w_file:
     data_file = csv.writer(w_file, delimiter='│', lineterminator="\r")
     data_file.writerow(["id_Name", "Name", "Age", "Telefon"])
     data_file.writerow(["159612", "Tom", "23", "5554378"])
     data_file.writerow(["310640", "Noah", "32", "5558732"])
     data_file.writerow(["044208", "Jacob", "41", "5559065"])
     data_file.writerow(["233648", "Liam", "21", "5552314"])
     data_file.writerow(["053872", "Michael", "27", "5550956"])
     data_file.writerow(["403600", "Anderson", " 54", "5552343"])


with open('name_three.csv', 'r', encoding='UTF-8') as r_file:
    file_reader = csv.reader(r_file, delimiter='│')
    count = 0