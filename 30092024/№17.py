def f(x):
    if x == 1:
        return 1
    if x % 2 != 0 and x > 1:
        return x + f(x - 2)
    return x * f(x - 1)

print(f(40))