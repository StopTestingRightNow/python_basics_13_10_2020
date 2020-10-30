"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

with open('Task5.txt', 'wt', encoding='UTF-8') as file:
    i = 0
    while i < 10:
        file.write(str(random.randint(1,100))+' ')
        i += 1

with open('Task5.txt', 'rt', encoding='UTF-8') as file:
    sum = 0
    content = file.read()
    for number in content.split():
        sum += int(number)

print(sum)
