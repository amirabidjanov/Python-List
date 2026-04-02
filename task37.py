list1 = [1, 2, 3]
list2 = [4, 5, 6]
i = 0
while i < len(list1):
    temp = list1[i]
    list1[i] = list2[i]
    list2[i] = temp

    i += 1

print(list1)
print(list2)