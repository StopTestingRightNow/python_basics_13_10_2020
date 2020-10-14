n = int(input("Введите число n: "))

num_of_digits = 0;
n_copy = n

while n_copy > 0:
    num_of_digits += 1
    n_copy = n_copy // 10

answer = (3 + 2 * (10 ** num_of_digits) + 10 ** (num_of_digits * 2)) * n

print(answer)
