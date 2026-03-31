royxat = []

while True:
    ism = input("ism kiriting: ")
    royxat.append(ism)
    if ism == "stop":
        if len(royxat) >= 5:
            print("ko'p element")
            break
        else:
            break

