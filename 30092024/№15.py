def func(x):
    v = []
    while x:
        x = x//5
        v.append(x % 5)
    return str(v[::-1])

print(func(25**5 + 5**14 - 5).count('4'))
