def func(x, step):
    if step == 3 and x >= 39:
        return 1
    elif step < 3 and x >= 39:
        return 0
    elif step == 3 and x < 39:
        return 0
    if step % 2 == 0:
        return func(x + 1, step + 1) or func(x + 2, step + 1) or func(x * 2, step + 1)
    return func(x + 1, step + 1) and func(x + 2, step + 1) and func(x * 2, step + 1)

step = 0
for i in range(1, 39):
    if func(i, step):
        print(i)
        break

for i in range(39, 1, -1):
    if func(i, step):
        print(i)
        break