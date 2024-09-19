def func(x):
    if x == 93:
        return 1
    elif x < 93:
        return func(x + 3) + func(x * 3)
    return 0
print(func(3))