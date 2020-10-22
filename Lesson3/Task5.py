"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def f_add_numbers(curr_sum, input_string):
    input_list = input_string.split()
    for string_number in input_list:
        if string_number == "q":
            return curr_sum
        curr_sum += float(string_number)
    return curr_sum


cursum = 0

while True:
    print(f"Current sum is {cursum}")
    numbers = input("Enter numbers to add or q to quit >>> ")
    cursum = f_add_numbers(cursum, numbers)
    if "q" in numbers:
        print(f"Final sum is {cursum}")
        break
