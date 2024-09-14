def func(x):
    while '52' in x or '2222' in x or '1122' in x:
        if '52' in x:
            x = x.replace('52', '11', 1)
        if '2222' in x:
            x = x.replace('2222', '5', 1)
        if '1122' in x:
            x = x.replace('1122', '25', 1)
    return x


n = 0
for i in range(10000, 3, -1):
    summ = 0
    n = i
    x = '5' + '2' * n
    x_after = func(x)
    for digit in x_after:
        summ += int(digit)

    if summ == 64:
        print(n)
        break


