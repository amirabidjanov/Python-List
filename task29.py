nums = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]
new_num = []
for num in nums:
    if nums.count(num) == 1:
        new_num.append(num)

print(new_num)