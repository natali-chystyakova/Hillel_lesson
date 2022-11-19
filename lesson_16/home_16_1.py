# Создайте свой произвольный класс и в нём помимо обычных методов и
# атрибутов создайте несколько статических методов и методов класса.
# Продемонстрируйте их работу.
import math

class Point():

    MIN = 0
    MAX = 100

    @classmethod
    def val(cls, args):
        return cls.MIN <= args <= cls.MAX

    @classmethod
    def attr_class(cls):
        return cls.MIN, cls.MAX, cls.un_of_meas()

    def __init__(self, x=0, y=0):
        self.x = self.y = 0
        if self.val(x) and self.val(y):
            self.x = x
            self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return (f"Point {self.x} {self.y}")

    @staticmethod
    def distance_from_origin(x, y):
        return math.hypot(x, y)

    @staticmethod
    def un_of_meas():
        return "units of measurement - centimeters"


a = Point(5, 4)
b = Point(5, 101)
print(b.x)
print(b.y)
print(Point.val(5))  # classmethod вызываем через класс

print(Point.attr_class())  # classmethod вызываем через класс
print(a.attr_class())  # classmethod вызываем через обьект

c = a + b
print(c)
print(Point.distance_from_origin(9, 10))  # staticmethod вызвали через класс
print(a.distance_from_origin(9, 10))  # staticmethod вызвали через обьект

print(Point.un_of_meas())  # staticmethod вызвали через класс
print(a.un_of_meas())  # staticmethod вызвали через обьект