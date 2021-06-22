# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый
# тип данных.

class Warehouse:
    def __init__(self, name, price, number, position, *args):
        self.name = name
        self.price = price
        self.number = number
        self.position = position
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Name': self.name, 'Price per unit': self.price, 'Quantity': self.number}

    def __str__(self):
        return f'{self.name} price {self.price}, quantity {self.number}'

    def acceptance(self):
        try:
            unit = input(f'Enter unit name: ')
            unit_pr = int(input(f'Enter price per unit: '))
            unit_num = int(input(f'Enter number of units: '))
            unique = {'Model': unit, 'Price per unit': unit_pr, 'Number of units': unit_num}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current list -\n {self.my_store}')
        except:
            return f'Input error'
        print('For exit press - Q, to continue press - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Total warehouse -\n {self.my_store_full}')
            return f'Exit'
        else:
            return Warehouse.acceptance(self)


class Printer(Warehouse):
    def to_print(self):
        return f'printing {self.numb} times'


class Scanner(Warehouse):
    def to_scan(self):
        return
        return f'scanning {self.numb} times'


class Copier(Warehouse):
    def to_copy(self):
        return
        return f'copying {self.numb} times'


unit_1 = Printer('Xerox', 10000, 20, 1, 12)
unit_2 = Scanner('Samsung', 8000, 3, 2, 12)
unit_3 = Copier('Braun', 4000, 15, 3, 10)
print(unit_1.acceptance())
print(unit_2.acceptance())
print(unit_3.acceptance())
print(unit_1.to_print())
print(unit_3.to_copy())
