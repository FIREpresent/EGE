def func(A):
    count = 0
    for m in range(1000):
        for n in range(1000):
            if (3 * m + 4 * n > 63) or ((m <= A) and (n < A)):
                count += 1
    if count == 1000*1000:
        return 1
    return 0

for x in range(100):
    if func(x):
        print(x)
        break

