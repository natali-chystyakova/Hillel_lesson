from home_14_1 import *
import time

# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение
# обязательного атрибута max_load.
# Создать по 2 объекта для каждого из классов truck и car,
# проверить все их методы и атрибуты.


class Truck(Auto):

    def __init__(self, brand, age,  mark, max_load, color="red", weight=12):
        super().__init__(brand, age,  mark, color, weight)
        self.max_load = max_load


    def move(self):
        print("attention")
        super().move()


    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)
        print(f"max load is {self.max_load}")



class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, color="red", weight=3):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed


    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


tr1 = Truck("Volkswagen", 5, "Crafter", 900)
tr2 = Truck("Peugeot", 3, "Crafter", 980)

print(tr1.brand)
print(tr2.brand)
print(tr1.age)
print(tr2.age)
print(tr1.mark)
print(tr2.mark)
print(tr1.max_load)
print(tr2.max_load)
print(tr1.color)
print(tr2.color)
print(tr1.weight)
print(tr2.weight)
tr1.move()
tr2.move()
tr1.load()
tr2.load()
tr1.stop()
tr2.stop()
tr1.birthday()
tr2.birthday()
tr1.birthday()
tr2.birthday()

car1 = Car("Audy", 3, "R8", 322)
car2 = Car("Opel", 1, "Kadett", 170)

print(car1.brand)
print(car2.brand)
print(car1.age)
print(car2.age)
print(car1.mark)
print(car2.mark)
print(car1.max_speed)
print(car2.max_speed)
print(car1.color)
print(car2.color)
print(car1.weight)
print(car2.weight)
car1.move()
car2.move()
car1.stop()
car2.stop()
car1.birthday()
car2.birthday()
car1.birthday()
car2.birthday()