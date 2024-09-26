def func(x):
    v = []
    while x:
        x //= 5
        n = x % 5
        v.append(n)
    return str(v[::-1])

s = func(125+25**3+5**9)
print(s.count('0'))

