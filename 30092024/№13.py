def func(x):
    while '00' not in x:
        x = x.replace('01', '220', 1)
        x = x.replace('02', '1013', 1)
        x = x.replace('03', '120', 1)
    return x

v = []
for x in range(50):
    for y in range(50):
        for z in range(50):
            num = '0' + '1'*x + '2'*y + '3'*z + '0'
            num = func(num)
            if num.count('1') == 13 and num.count('2') == 18:
                v.append(x + y + z)
print(max(v) + 2)