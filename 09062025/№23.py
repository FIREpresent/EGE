def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x-1, y) + f(x - (x % 10) if x % 10 != 0 else x - 2, y) + f(x//2, y)

print(f(47, 40)*f(40, 18)*f(18, 14))