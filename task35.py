words = ["kitob", "dastur", "AI", "hello", "python", "assalomu alaykum"]

group1 = []
group2 = []
group3 = []

for word in words:
    if len(word) <= 3:
        group1.append(word) 
    elif len(word) <= 6:
        group2.append(word)
    else:
        group3.append(word)

print(group1)
print(group2)
print(group3)