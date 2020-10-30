"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('Task1.txt', 'wt', encoding='UTF-8') as file:
    while True:
        s_line = input('Enter the line >>> ')
        if not s_line:
            break
        file.write(s_line + '\n')
