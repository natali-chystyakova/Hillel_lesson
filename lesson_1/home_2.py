a = 5

b = 'text '

print(type(a))

print(type(b))

a = b + '!'
print(type(a))
print(a)
c = b * 5
print(c)
print(len(c))
print(c[1])  # показать второй символ слова 'text '
print(c[-1])  # показать последнюю букву
print(c[-3])  # показть третью с конца
print(c[1:3])  # с первого до третьего, не включая его - ex прямая печать индексов 1-2
print(c[-3:-1])  # напечаталось ex прямая печать индексов 1-2 ex прямая печать индексов 1-2 - то же самое
print(c[0:-1:2]) # с первого по последний с шагом 2
print(c[::2])  # с первого по последний - если пусто
print(c[::-1])  # в обратном порядке !!!
print(c.upper())
print(c.title()) #  Text Text Text Text Text
b = None
print(id(c))  # id разные. Конкретно у этой ячейки свой
g = None
print(id(g))  # id а у этой - свой

a = 5
s = 5
print(id(a))  # одинаковые   id
print(id(s))
print(a is s)  #True - сравниваются не значения а id(a) и id(b)

print('for git')