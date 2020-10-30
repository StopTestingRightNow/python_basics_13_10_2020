"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


with open('Task4.txt', 'rt', encoding='UTF-8') as file:
    with open('Task4_2.txt', 'wt', encoding='UTF-8') as w_file:
        content = file.readlines()
        for line in content:
            line = line.replace("One","Один", 1)
            line = line.replace("Two","Два", 1)
            line = line.replace("Three","Три", 1)
            line = line.replace("Four","Четыре", 1)
            print(line)
            w_file.write(line)
