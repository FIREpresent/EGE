def f(x, step):
    if (step == 2 or step == 4) and x >= 40:
        return 1
    elif step == 4 and x < 40:
        return 0
    elif x >= 40 and step < 4:
        return 0
    else:
        if step % 2 != 0:
            return f(x + 1, step + 1) or f(x + 4, step + 1) or f(x * 2, step + 1)
        else:
            return f(x + 1, step + 1) and f(x + 4, step + 1) and f(x * 2, step + 1)


def f1(x, step):
    if step == 2 and x >= 40:
        return 1
    elif step == 2 and x < 40:
        return 0
    elif x >= 40 and step < 2:
        return 0
    else:
        if step % 2 != 0:
            return f1(x + 1, step + 1) or f1(x + 4, step + 1) or f(x * 2, step + 1)
        else:
            return f1(x + 1, step + 1) and f1(x + 4, step + 1) and f(x * 2, step + 1)


for x in range(1, 40):
    if f(x, 0) == 1:
        print(x)
        
for x in range(1, 40):
    if f1(x, 0) == 1:
        print(x)