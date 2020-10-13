income = int(input("Доход: "))
expenses = int(input("Расход: "))

profit = income - expenses

if profit > 0:
    print("Фирма приносит прибыль, рентабельность - ", profit/income)
    num_of_employees = int(input("Число сотрудников: "))
    print("Прибыль на одного сотрудника: ", profit/num_of_employees)
elif profit == 0:
    print("Фирма безубыточна")
else:
    print("Фирма убыточна")