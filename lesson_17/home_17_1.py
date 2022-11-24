# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень
# и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких
# исключений, как минимум деление на 0.
#
# Создать своё исключение, к примеру возведение в отрицательную степень.

import math
class Calculator():
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        try:
            z = self.x + other.x
        except TypeError:
            print("TypeError")
            self.x = None
            other.x = None

        else:
            return Calculator(z)

    def __sub__(self, other):
        try:
            z = self.x - other.x
            if other.x > self.x:
                raise ValueError
        except TypeError as error:
            print ("TypeError")
            self.x = None
            other.x = None
        except ValueError:
            print("Нельзя вычитать из меньшего числа - большее")
            z = other.x - self.x
            return Calculator(z)

        else:
            return Calculator(z)

    def __mul__(self, other):
        try:
            z = self.x * other.x
            if self.x < 0 or other.x < 0:
                raise ValueError
        except TypeError:
            print("TypeError")
            self.x = None
            other.x = None
        except ValueError:
            print("Нельзя перемножать отрицательные числа")
            z = abs(self.x * other.x)
            return Calculator(z)
        else:
            return Calculator(z)

    def __truediv__(self, other):
        try:
            z = self.x / other.x
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            if other.x == 0:
                return Calculator(x=0)
        else:
            return Calculator(z)

    def __pow__(self, other):

        try:
            z = self.x ** other.x
            if other.x < 0:
                raise NegativePowerException
        except NegativePowerException:
            print("Нельзя возводить в отрицательную степень")
            return self.x ** abs(other.x)
        except TypeError:
            print("TypeError")
            if other.x == 0:
                Calculator(x=1)
        else:
            return Calculator(z)


    def sqrt(self):
        try:
            self.x = math.sqrt(self.x)

        except ValueError:
            print("ValueError. Нельзя извлекать корень из отрицательного числа")
            if self.x < 0:
                return math.sqrt(abs(self.x))

    def __str__(self):
        return f"{self.x}"


class NegativePowerException(BaseException):
    pass

a = Calculator(5)
b = Calculator(-2)

c = a + b
print(c)

c = a - b
print(c)

c = a * b
print(c)

c = a / b
print(c)

c = a ** b
print(c)

v = Calculator(-25)
print(v.sqrt())
