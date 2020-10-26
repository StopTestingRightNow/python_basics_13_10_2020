"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

scriptname, worktime, rate, bonus = argv

def f_wage(worktime, rate, bonus):
    return (worktime * rate) + bonus


print(f_wage(float(worktime), float(rate), float(bonus)))
