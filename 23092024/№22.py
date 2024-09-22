def func(x, step):
    if (step == 2 or step == 4) and x >= 32:
        return 1
    elif step < 4 and x >= 32:
        return 0
    elif step == 4 and x < 32:
        return 0
    else:
        if x % 2 != 0:
            return func(x + 1, step + 1) or func(x * 3 + 1, step + 1)
        else:
            return func(x + 1, step + 1) and func(x * 3 + 1, step + 1)

def func1(x, step):
    if step == 2 and x >= 32:
        return 1
    elif step < 2 and x >= 32:
        return 0
    elif step == 2 and x < 32:
        return 0
    else:
        if x % 2 != 0:
            return func(x + 1, step + 1) or func(x * 3 + 1, step + 1)
        else:
            return func(x + 1, step + 1) and func(x * 3 + 1, step + 1)


step = 0
for i in range(1, 32):
    if func(i, step) and func1(i, step):
        print(i)