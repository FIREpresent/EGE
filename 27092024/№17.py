def func(x):
    if x == 1 or x == 2:
        return 1
    return func(x - 2) * x

print(func(7))
