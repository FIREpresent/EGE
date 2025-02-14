from itertools import product

count = 0
alphabet = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
for i in range(1, 7):
    for c in product(alphabet, repeat=i):
        count += 1
        s = "".join(c)
        if s == "FDECBA":
            print(count)
            break