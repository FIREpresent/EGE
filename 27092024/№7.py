def func(x):
    v = []
    sum1, sum2, sum3 = int(x[0]) + int(x[1]), int(x[1]) + int(x[2]), int(x[2]) + int(x[3])
    deleted_sum = min(sum1, sum2, sum3)
    v.append(sum1)
    v.append(sum2)
    v.append(sum3)
    v.pop(v.index(min(v)))
    return str(min(v)) + str(max(v))

for x in range(9999, 999, -1):
    res = int(func(str(x)))
    if res == 1315:
        print(x)
        break
