# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumbers:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'total c1 and c2 is: ')
        return f'c = {self.a + other.a} +{self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Intersection c1 and c2 is: ')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c1 = ComplexNumbers(2, -4)
c2 = ComplexNumbers(5, 4)
print(c1)
print(c1 + c2)
print(c1 * c2)
