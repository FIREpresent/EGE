
def func(x, step):
    if x >= 96 and step % 2 != 0:
        return 1
    elif x >= 96 and step % 2 == 0:
        return 0

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



step = [1, 3, 5]
for x in range(96, 0, -1):
    if not func(x, step[0]) and func(x, step[1]) and func(x, step[2]):
        print(x)
        break
