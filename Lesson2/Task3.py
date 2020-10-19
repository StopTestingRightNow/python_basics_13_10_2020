month_list = ["Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Autumn", "Autumn",
              "Autumn", "Winter"]
month_dict = {"Winter": {1, 2, 12},
              "Spring": {3, 4, 5},
              "Summer": {6, 7, 8},
              "Autumn": {9, 10, 11}}

month_num = int(input("Enter month number "))

print(f"By list the season is {month_list[month_num - 1]}")

for key in month_dict.keys():
    if month_num in month_dict[key]:
        print(f"By dictionary the season is {key}")
        break
