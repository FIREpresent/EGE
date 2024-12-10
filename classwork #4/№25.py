from itertools import *


def func(x):
    p = [2, 3]
    arr = set(p)
    v = []
    s = []
    for d in range(2, int((x**0.5))+1):
        flag = True
        for dels in list(arr):
            if d >= 4:
                if d % dels == 0:
                    flag = False
                    break
        if flag:
            v.append(d)
            arr.add(d)

    for i in range(len(v)):
        while x % v[i] == 0:
            s.append(v[i])
            x /= v[i]
    s = sorted(s)
    # print(f's: {s}')

    b = sorted(combinations(s, r=2))
    c = sorted(combinations(s, r=3))
    d = sorted(combinations(s, r=4))
    e = sorted(combinations(s, r=5))

    for y in b:
        s.append(y[0] * y[1])
    for y in c:
        s.append(y[0] * y[1] * y[2])
    for y in d:
        s.append(y[0] * y[1] * y[2] * y[3])
    for y in e:
        s.append(y[0] * y[1] * y[2] * y[3] * y[4])
    # print(p)
    return sorted(list(set(s)))[:5]

count = 0
num = 5_000_000_001
while count < 5:
    n = func(num)
    if len(n) >= 5 and n[0] * n[1] * n[2] * n[3] * n[4] < num:
        print(n[0] * n[1] * n[2] * n[3] * n[4], num)
        count += 1
    num += 1
