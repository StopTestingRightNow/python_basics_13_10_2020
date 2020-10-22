"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def two_of_three(a, b, c):
    al, bl, cl = int(a), int(b), int(c)
    if cl >= al <= bl:
        return cl + bl
    elif bl >= cl:
        return al + bl
    return al + cl


a, b, c = input("Enter three numbers >>> ").split()
print(f"The result is >>> {two_of_three(a, b, c)}")
