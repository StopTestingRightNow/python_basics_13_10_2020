import math

a = int(input("Исходный результат: "))
b = int(input("Искомый результат: "))
increment_factor = 1.1

answer = math.ceil(math.log(b/a, increment_factor))+1

print(f"Ответ: на {answer}-й день спортсмен достиг результата — не менее {b} км.")
