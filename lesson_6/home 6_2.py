# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for

input_value = int(input("введите целое число"))
q = 0
result = 0
while input_value > q:
    q = q + 1
    if q % 3 == 0:
        continue

    result += q ** 3

print("result to while", result)

result = 0
for item in range(1, input_value + 1):
    if item % 3 == 0:
        continue
    result += item**3

print("result to for", result)
