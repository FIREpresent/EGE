
def func(x):
    para1 = int(x[0]) + int(x[1])
    para2 = int(x[2]) + int(x[3])

    if para1 > para2:
        return int(str(para2) + str(para1))
    return int(str(para1) + str(para2))

count = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0 and func(str(i) + str(j) + str(k) + str(l)) == 616:
                    count += 1
print(count)