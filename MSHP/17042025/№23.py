def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 11 if x % 10 != 9 else x + 10, y)

print(f(26, 49))
