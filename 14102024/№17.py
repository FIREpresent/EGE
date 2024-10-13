def func(x):
    v = []
    while x:
        v.append(x % 7)
        x = x // 7
    return str(v[::-1])

print(func(49**10 + 7**30 - 49).count('6'))

