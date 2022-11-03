# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

line1 = input("введите строку 1: ") + "\n"
line2 = input("введите строку 2: ") + "\n"
line3 = input("введите строку 3: ") + "\n"
line4 = input("введите строку 4: ") + "\n"

list_line = [line1, line2, line3, line4]
with open("test12.txt", "w") as f:
    for index, item in enumerate(list_line):
        if index <= 1:
            f.write(item)

with open("test12.txt", "a") as f:
    for index, item in enumerate(list_line):
        if index > 1:
            f.write(item)