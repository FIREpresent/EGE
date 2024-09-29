def func(x):
    if x > 15:
        return 0
    elif x == 15:
        return 1
    return func(x + 1) + func(x + 4)

print(func(3))