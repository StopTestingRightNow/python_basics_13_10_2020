"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re
import My_Implements

result = {}
with open('Task6.txt', 'rt', encoding='UTF-8') as file:
    content = file.readlines()
    for index, line in enumerate(content):
        content[index] = line.split()
        key = re.search(r'\w+', content[index][0]).group()
        string_list = content[index][1::]
        for index2, entry in enumerate(string_list):
            hours_value = re.search(r'\d+', entry)
            if hours_value:
                string_list[index2] = int(hours_value.group())
            else:
                string_list[index2] = 0
        result[key] = My_Implements.my_sum(*string_list)

print(result)
