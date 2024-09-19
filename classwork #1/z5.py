with open("1.txt") as f:
    m = f.readlines()
    # f = open("1.txt")
    for s in f:
        print(s)
print(m)
f.close()