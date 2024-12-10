def func(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return 0
    return 1

v = []
for x in range(1, 100):
    for y in range(1, 100):
        a =  '0' + '1' * x + '2' * y
        if len(a) > 44:
            b = '0' + '1' * x + '2' * y
            while '01' in b or '02' in b:
                b = b.replace('02', '1110', 1)
                b = b.replace('01', '220', 1)
            if func(sum(list(map(int, list(b))))):
                v.append(sum(list(map(int, list(a)))))
print(min(v))
