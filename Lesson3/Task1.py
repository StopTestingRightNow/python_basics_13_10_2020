"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def f_division(divided, divisor):
    divided_f = float(divided)
    divisor_f = float(divisor)
    if divisor_f == 0:
        if divided_f == 0:
            return float("nan")
        return float("inf")
    return divided_f / divisor_f


print(f"Result >>>", f_division(input("Enter divided >>> "), input("Enter divisor >>> ")))
