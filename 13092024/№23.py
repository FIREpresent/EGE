def func(x):
    if x == 31:
        return 1
    elif x > 31:
        return 0
    return func(x+1) + func(x+10)

print(func(10))

