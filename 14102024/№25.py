def f(x, step):
    if (step == 2 or step == 4) and x >= 43:
        return 1
    elif step < 4 and x >= 43:
        return 0
    elif step == 4 and x < 43:
        return 0
    else:
        if step % 2 != 0:
            return f(x + 1, step + 1) or f(x + 2, step + 1) or f(x * 2, step + 1)
        return f(x + 1, step + 1) and f(x + 2, step + 1) and f(x * 2, step + 1)

for x in range(1, 43):
    if f(x, 0):
        print(x)
        break