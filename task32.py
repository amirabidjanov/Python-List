royxat = ["kitob", "dastur", "AI", "hello", "python"]

filter = []
for word in royxat:
    if len(word) >= 5:
        filter.append(word)

print(filter)