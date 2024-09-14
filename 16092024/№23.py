def func(x):
    if x == 32:
        return 1
    elif x > 32:
        return 0
    return func(x+1) + func(x+10)

print(func(10))