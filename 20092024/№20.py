def func(x, step):
    if step == 3 and x >= 64:
        return 1
    elif step == 3 and x < 64:
        return 0
    elif step < 3 and x >= 64:
        return 0
    else:
        if step % 2 == 0:
            return func(x + 1, step + 1) or func(x + 2, step + 1) or func(x * 3, step + 1)
        else:
            return func(x + 1, step + 1) and func(x + 2, step + 1) and func(x * 3, step + 1)


step = 0
for i in range(1, 64):
    if func(i, step):
        print(i)