# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionNull:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.dividend = dividend

    @staticmethod
    def devide_null(divider, dividend):
        try:
            return (divider / dividend)
        except:
            return (f'Деление на ноль невозможно!')


div = DivisionNull(2, 100)
print(DivisionNull.devide_null(2, 0))
print(DivisionNull.devide_null(2, 0.1))
print(div.devide_null(200, 2))
