"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


with open('Task3.txt', 'rt', encoding='UTF-8') as file:
    content = file.readlines()
    num_of_employees = len(content)
    wage_sum = 0
    for record in content:
        employee, wage = record.split()
        wage = int(wage)
        wage_sum += wage
        if wage < 20000:
            print(f'Employee {employee} earns less than 20000')
    print(f'Average wage is {wage_sum/num_of_employees}')
