def func(x):
    while '01' in x or '02' in x or '03' in x:
            x = x.replace('01', '2302', 1)
            x = x.replace('02', '10', 1)
            x = x.replace('03', '201', 1)
    return x

num = 0
for i in range(1, 40):
    for j in range(1, 40):
        for k in range(1, 40):
            x = '0' + i*'1' + j*'2' + k*'3'
            x = func(x)
            if x.count('1') == 40 and x.count('2') == 10 and x.count('3') == 8:
                num = i
                break

print(num)
