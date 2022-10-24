# Дан список чисел.
# Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь (ключ - само число,
# а значение - сколько раз оно встречается). Для проверки нахождения элемента
# в словаре использовать метод get(), либо оператор in.

list_1 = [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]


def how_many_times(list, elem):
    dict = {i: list.count(i) for i in list}
    desired_number = dict.get(elem)
    word = "раза" if desired_number != None and desired_number % 10 in [2, 3, 4] else "раз"

    if desired_number != None:
        answer = f"данный елемент встречается {desired_number} {word} "
    else:
        answer = "такого елемента нет в списке"

    return dict, answer


output_dict, answer_times = how_many_times(list_1, 5)
print(output_dict)
print(answer_times)