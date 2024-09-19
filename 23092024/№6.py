def func(x):
    para1 = int(x[0]) + int(x[1])
    para2 = int(x[1]) + int(x[2])

    if para1 > para2:
        return int(str(para2) + str(para1))
    return int(str(para1) + str(para2))

for n in range(100, 1000):
    if func(str(n)) == 714:
        print(n)
        break