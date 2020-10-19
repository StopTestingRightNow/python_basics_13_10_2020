rating_list = [7, 5, 3, 3, 2]
rating_count = len(rating_list)
rating_min = min(rating_list)
rating_max = max(rating_list)

while True:
    print("Current ratings: ", rating_list)
    new_num_str = input("Enter new number or q for finish ")
    if new_num_str == "q":
        break
    new_num = int(new_num_str)
    position_found = False
    if new_num <= rating_min:
        rating_list.append(new_num)
        rating_min = new_num
        continue
    if new_num > rating_max:
        rating_list.insert(0, new_num)
        rating_max = new_num
        continue

    start_index = 0
    end_index = rating_count - 1
    insert_index = 0
    while not position_found:
        lookup_index = (start_index + end_index) // 2
        lookup_value = rating_list[lookup_index]
        lookup_value_right = rating_list[lookup_index + 1]
        if new_num == lookup_value:
            position_found = True
            insert_index = lookup_index + 1
        elif lookup_value > new_num >= lookup_value_right:
            position_found = True
            insert_index = lookup_index + 1
        elif lookup_value > new_num:
            start_index = lookup_index
        elif lookup_value < new_num:
            end_index = lookup_index

    while not rating_list[insert_index + 1] < new_num:
        insert_index += 1

    rating_list.insert(insert_index, new_num)
