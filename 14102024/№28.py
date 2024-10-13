def f(x, c):
    if x > 11:
        return 0
    if x == 11:
        return 1
    elif not c:
        return f(x + 1, 0) + f(x + 2, 0) + f(2*x, 1)
    return f(x + 1, 0) + f(x + 2, 0)

print(f(1, 0))