def func(x, step):
    if step == 2 and x >= 32:
        return 1
    elif step < 2 and x >= 32:
        return 0
    elif step == 2 and x < 32:
        return 0
    return func(x + 1, step + 1) or func(x * 3 + 1, step + 1)


step = 0
for i in range(1, 32):
    if func(i, 0):
        print(i)
        break