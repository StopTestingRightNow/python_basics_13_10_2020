"""
zip
map
reduce
sorted
max
min
sum
range
round
divmod
"""

def exponentiation(x, y):
    return x ** y


def exponentiation2(x, y):
    y = abs(y) - 1
    while y > 0:
        x *= x
        y -= 1
    return 1 / x


try:
    user_x = float(input('Введите положительный x:\n>>> '))
    user_y = int(input('Введите отрицательный y:\n>>> '))
    if user_x > 0:
        if user_y < 0:
            answer = input('1.Возвести используя оператор **\n2.Возвести НЕ используя оператор **\n>>>')
            if answer == '2':
                print(f'Результат БЕЗ использования **: {exponentiation2(user_x, user_y)}')
            else:
                print(f'Результат с использованием **: {exponentiation(user_x, user_y)}')
        else:
            print('Написано же отрицательное!')
    else:
        print('Написано же Положительное!')
except ValueError:
    print('Нужно вводить числа')
