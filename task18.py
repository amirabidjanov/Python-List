royxat = []

while True:
    ism = input("ism kiriting: ")
    royxat.append(ism)
    if ism == "stop":
        if (len(royxat) - 1) // 2 == 0:
            print("False")
            if ism == "stop":
                break
        else:
            print("True")
            if ism == "stop":
                break