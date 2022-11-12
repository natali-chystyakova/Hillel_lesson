# *Для рассмотренного на уроке класса Circle реализовать метод производящий
# вычитание двух окружностей, вычитание радиусов произвести по модулю.
# Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.

import math
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return (f"Point({self.x}, {self.y})")

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        # center = super().__add__(other)
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __abs__(self):
        return abs(self.radius), abs(self.x), abs(self.y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Circle(radius, x, y)

    def __str__(self):
        if self.radius == 0:
            return super().__str__()
        else:
            return 'Circle' + super().__str__()[5:] + f', radius={self.radius}'


    def area(self):
        return math.pi * (self.radius ** 2)

    def circle_weight(self):
        return 2 * math.pi * self.radius


m = Circle(6, 2, 3)
n = Circle(3)
l = Circle(56, 5, 7)

z = m - l
print(z)

z = n - m
print(z)
g = Circle(-6, -2, -3)
c = abs(g)
print(c)