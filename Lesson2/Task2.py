initial_list = input("Enter initial list ").split()

count = len(initial_list) // 2

i = 0
while i < count:
    initial_list[i * 2], initial_list[i * 2 + 1] = initial_list[i * 2 + 1], initial_list[i * 2]
    i += 1

print(initial_list)
