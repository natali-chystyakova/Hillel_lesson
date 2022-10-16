# Сделать программу в виде функций в которой нужно будет угадывать число.
import random

def guess_number():
    guesses_time = 0
    number_guess = random.randint(1, 10)
    print("Угадайте число от 1 до 10. У вас есть 3 попытки")
    while guesses_time < 3:
        number = input("Введите число от 1 до 10: ")

        if not number.isdigit():
            print("Это не число. Повторите ввод")
            continue

        elif int(number) == number_guess:
            print("Все верно. Вы угадали")
            break
        elif int(number) < number_guess:
            print("Ваше число меньше загаданного")
        else:
            print("Ваше число больше загаданного")
        guesses_time = guesses_time + 1
    return int(number), number_guess


number, number_guess = guess_number()
print(number)
print(number_guess)


def valid():
    if number != number_guess:
        return f"Вы не угадали. Это было число {number_guess}"
    else:
        return f"Все верно. Это было число {number_guess}"


print(valid())