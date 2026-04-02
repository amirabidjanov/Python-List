list = ["kitob", "dastur", "AI", "hello", "python"]
uzun = list[0]
for soz in list:
    if len(soz) > len(uzun):
        uzun = soz
print(soz)