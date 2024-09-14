
def func(x, step):
    if x >= 96:
        return 1

    if step == -1:
        return 0

    results = [func(x + 1, step - 1)]
    if x % 2 == 0:
        results += [func(x + x // 2, step - 1)]

    if x % 3 == 0:
        results += [func(x + x // 3, step - 1)]

    if x % 2 != 0 and x % 3 != 0:
        results += [func(x * 2, step - 1)]

    if step % 2 == 0:
        return any(results)
    return all(results)



step = 1
for x in range(1, 96):
    if func(x, step):
        print(x)
        break