def func(x):
    if x == 36:
        return 1
    elif x > 36:
        return 0
    return func(x + 1) + func(x * 3)

print(func(3))