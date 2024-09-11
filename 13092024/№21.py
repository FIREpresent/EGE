def func(x, step):
    if (step == 2 or step == 4) and x >= 39:
        return 1
    elif step < 4 and x >= 39:
        return 0
    elif step == 4 and x < 39:
        return 0
    if step % 2 != 0:
        return func(x + 1, step + 1) or func(x + 2, step + 1) or func(x * 2, step + 1)
    return func(x + 1, step + 1) and func(x + 2, step + 1) and func(x * 2, step + 1)

def func2(x, step):
    if step == 2 and x >= 39:
        return 1
    elif step < 2 and x >= 39:
        return 0
    elif step == 2 and x < 39:
        return 0
    if step % 2 != 0:
        return func(x + 1, step + 1) or func(x + 2, step + 1) or func(x * 2, step + 1)
    return func(x + 1, step + 1) and func(x + 2, step + 1) and func(x * 2, step + 1)

step = 0
for i in range(1, 39):
    if func(i, step):
        print(i)

for i in range(1, 39):
    if func2(i, step):
        print(i)