list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
list = []
for item in list1:
    if item in list2:
        list.append(item)

print(list)