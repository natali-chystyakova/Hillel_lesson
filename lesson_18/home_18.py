# Создать генератор геометрической прогрессии
# first_value - первый елемент
# step - множитель
# n - количество иттераций

def geom_progr(first_value, step, n):
    iter = 0
    while iter < n:
        b_cur = first_value
        yield b_cur
        first_value = b_cur * step
        iter += 1


a = geom_progr(1, 7, 5)

for item in a:
    print(item)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))