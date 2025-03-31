def func(x, base):
    v = []
    while x:
        v.append(x % base)
        x = x // base
    return str(v[::-1])

print(func(2*216**6 + 3*36**9 - 432, 6).count('5'))