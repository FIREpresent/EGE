

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


v = []
step = [0, 2]
for x in range(96, 0, -1):
    if not func(x, step[0]) and func(x, step[1]):
        v.append(x)
    if len(v) == 2:
        break

print(*sorted(v))