# Прочитать сохранённый json-файл из задания №17 и записать данные
# на диск в csv-файл, первой строкой которого озаглавив каждый
# столбец и добавив новый столбец “телефон”.
import json
import csv


with open("home_13_01.json", "r") as f:
    output_j_dict = json.load(f)

print("output_j_dict:\n", output_j_dict)

name_of_fields = ["ID", "Name", "Age", "Phone"]
phones = [1111, 2222, 3333, 4444, 5555]

with open("home_13_02.csv", "w", encoding="utf-8", newline='') as f1:
    file_writer = csv.writer(f1)
    count = 0
    for key, value in (output_j_dict.items()):

        value.insert(0, key)

        value.insert(4, phones[count])

        if count == 0:
            file_writer.writerow(name_of_fields)
        count += 1

        file_writer.writerow(value)