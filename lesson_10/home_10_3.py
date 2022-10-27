#ДЗ 12
# Написать декоратор к 2-м любым функциям, который бы считал и
# выводил время их выполнения.

from datetime import datetime

def decorator_time(a_func):
    def wraper(*args, **kwargs):
        time = datetime.now()
        a_func(*args, **kwargs)
        all_time = datetime.now()-time
        print("Время выполнения функции: ",  all_time, "секунд")
        return a_func(*args, **kwargs)
    return wraper


@decorator_time
def sum_list():
    return sum([number for number in range(10000)])


print(sum_list())


@decorator_time
def func(number):
    rez = 1
    for num in range(1, number+1):
        rez *= num
    return rez


print(func(1000))