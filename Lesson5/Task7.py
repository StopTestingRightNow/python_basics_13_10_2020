"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open('Task7.txt', 'rt', encoding='UTF-8') as file:
    context = file.readlines()
    num_of_firms = len(context)
    total_profit = 0
    result = [{}, {}]
    for line in context:
        firm_strings = line.split()
        key = firm_strings[0]
        profit = int(firm_strings[2]) - int(firm_strings[3])
        if profit > 0:
            total_profit += profit
        result[0][key] = profit
    result[1]["average_profit"] = total_profit / num_of_firms
    with open("Task7.json", "wt") as write_file:
        json.dump(result, write_file)
