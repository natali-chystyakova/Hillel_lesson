# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto:
    count = 1

    def __init__(self, brand, age,  mark, color="red", weight=3):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight


    def move(self):
        print("«move»")

    def stop(self):
        print("«stop»")

    def birthday(self):

        birthday = self.count + self.age
        self.count = self.count + 1

        print(birthday)


aut_1 = Auto("audy", 3, "R8")
aut_1.birthday()
aut_1.birthday()
aut_1.birthday()
aut_1.move()
aut_1.stop()