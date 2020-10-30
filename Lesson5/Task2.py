"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


with open('Task2.txt', 'rt', encoding='UTF-8') as file:
    content = file.readlines()
    print(f'File contains {len(content)} lines')
    for index, line in enumerate(content, 1):
        print(f'Line number {index} contains {len(line.split())} words')
