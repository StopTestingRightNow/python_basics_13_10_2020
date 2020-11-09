"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой. """


class DivByZero(Exception):
    pass


def division(a, b):
    try:
        try:
            return a/b
        except ZeroDivisionError:
            raise DivByZero()
    except DivByZero:
        print('Division by zero. Result will be float(\'inf\')')
        return float('inf')


print(division(2, 0))
