"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def f_inline(**kwargs):
    return str(kwargs.items())


user_template = {
    "имя": ("имя пользователя", str),
    "фамилия": ("фамилию пользователя", str),
    "год рождения": ("год рождения пользователя", int),
    "город проживания": ("город проживания", str),
    "email": ("email", str),
    "телефон": ("контактный телефон", str)
}

user_record = {}

for key, value in user_template.items():
    while True:
        user_value = input(f'Введите {value[0]}\n')
        try:
            user_value = value[1](user_value)
        except ValueError as e:
            print(f"{e}\nНеверный формат данных")
            continue
        user_record[key] = user_value
        break

print(f_inline(**user_record))
