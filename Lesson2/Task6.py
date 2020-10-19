goods_list = []
goods_count = 0

while True:
    input_list = input("Enter name, price, quantity and units of measurement (or q to quit) >>> ").split()
    if input_list == ["q"]:
        break
    goods_count += 1
    goods_list.append((goods_count, {"name": input_list[0], "price": input_list[1], "quantity": input_list[2],
                                     "unit": input_list[3]}))
    print("Current goods are:")
    print(*goods_list, sep="\n")

analytics_dic = {}

for good in goods_list:
    for goods_key, goods_value in good[1].items():
        if analytics_dic.get(goods_key) is None:
            analytics_dic[goods_key] = set()
        analytics_dic[goods_key].add(goods_value)


print("Current analytics are:")
for key, values in analytics_dic.items():
    print(key+": ", values)
