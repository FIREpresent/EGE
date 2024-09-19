def func(x):
    if x == 30:
        return 1
    elif x > 30:
        return 0
    return func(x+1) + func(x+2) + func(x+5)

print(func(21))