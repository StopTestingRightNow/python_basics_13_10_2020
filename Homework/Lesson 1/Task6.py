a = float(input("Исходный результат: "))
b = int(input("Искомый результат: "))
increment_factor = 1.1

answer = 1

while a < b:
    answer += 1
    a *= increment_factor

print(f"Ответ: на {answer}-й день спортсмен достиг результата — не менее {b} км.")
