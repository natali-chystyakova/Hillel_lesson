# Созадать словарь в качестве ключа которого будет 6-ти значное число,
# а в качестве значений кортеж состоящий из 2-х элементов – имя(str),
# возраст(int).  Сделать около 5-6 элементов словаря.
# Записать данный словарь на диск в json-файл.
import json

j_dict = {
    100001: ("Masha", 20),
    100002: ("Natali", 30),
    100003: ("Alex", 4),
    100004: ("Anna", 40),
    100005: ("Olga", 35)

}

with open("home_13_01.json", "w") as f:
    json.dump(j_dict, f)

