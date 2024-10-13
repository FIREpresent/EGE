
for x in range(2, 3000):
    y = bin(x)[2:]
    y = y[:-1]
    if x % 2 != 0:
        y += '10'
    else:
        y += '01'
    num = int(y, 2)
    if num == 2018:
        print(x)
