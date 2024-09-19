def func1(x, step):
    if step == 2 and x >= 64:
        return 1
    elif step == 2 and x < 64:
        return 0
    elif step < 2 and x >= 64:
        return 0
    else:
        if step % 2 != 0:
            return func1(x + 1, step + 1) or func1(x + 2, step + 1) or func1(x * 3, step + 1)
        else:
            return func1(x + 1, step + 1) and func1(x + 2, step + 1) and func1(x * 3, step + 1)

def func2(x, step):
    if (step == 2 or step == 4) and x >= 64:
        return 1
    elif step == 4 and x < 64:
        return 0
    elif step < 4 and x >= 64:
        return 0
    else:
        if step % 2 != 0:
            return func2(x + 1, step + 1) or func2(x + 2, step + 1) or func2(x * 3, step + 1)
        else:
            return func2(x + 1, step + 1) and func2(x + 2, step + 1) and func2(x * 3, step + 1)


for i in range(1, 64):
    if func1(i, 0) == 0 and func2(i, 0) == 1:
        print(i)