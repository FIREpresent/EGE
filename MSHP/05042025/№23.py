def f(x, y):
    if x < y or x == 32:
        return 0
    elif x == y:
        return 1
    return f(x//4, y) + f(x-1, y) + f(x-5, y)

print(f(43, 39)*f(39,17))