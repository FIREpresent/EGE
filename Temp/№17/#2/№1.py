def func(x):
    dels = []
    for d in range(2, int(elem ** 0.5) + 1):
        if elem % d == 0:
            dels.append(d)
    if len(dels)+2 > 15:
        dels.clear()
        return 1
    return 0

count = 0
maximum = -10**10
for elem in range(12356, 76435):
    if func(elem):
        count += 1
        maximum = max(maximum, elem)

print(count, maximum)