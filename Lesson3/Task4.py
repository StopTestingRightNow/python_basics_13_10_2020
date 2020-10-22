"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def f_power_default (a,b):
    return float(a)**int(b)

def f_power_custom (a,b):
    a = float(a)
    b = int(b)
    base = a
    b += 1
    while b<0:
        base *= a
        b += 1
    return 1 / base


a, b = input("Enter base and power >>> ").split()
print(f"Result from default power function>>> {f_power_default (a,b)} \n"
      f"Result from custom power function>>> {f_power_custom (a,b)}")
