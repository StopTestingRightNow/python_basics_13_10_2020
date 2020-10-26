"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
import itertools

start = 3

for x in itertools.count(start=start, step=1):
    print(x, end=' ')
    if x == 10:
        break

print("\n\n")

initial_list = [2, 7, 23, 1, 44, 3, 2, 10, 7, 4, 11]

counter = 0

for x in itertools.cycle(initial_list):
    print(x, end=' ')
    counter += 1
    if counter >= 20:
        break