def func(x, step):
    if step == 2 and x >= 64:
        return 1
    elif step < 2 and x >= 64:
        return 0
    elif step == 2 and x < 64:
        return 0
    return func(x + 1, step + 1) or func(x + 2, step + 1) or func(x * 3, step + 1)

step = 0
for i in range(1, 64):
    if func(i, step):
        print(i)
        break