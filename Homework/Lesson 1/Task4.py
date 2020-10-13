n = int(input("Введите число n: "))
answer = 0

while n > 0:
    digit = n % 10
    n = n//10
    if digit > answer:
        answer = digit

print(f"Самая большая цифра десятичной записи числа n - {answer}")
