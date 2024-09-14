def func(x, v):
    if x.count('А') == 3 and x.count('П') == 1 and x.count('Р') == 1 and x.count('Б') == 1 and x.count('Л') == 1 and x.count('О') == 1:
        for y in range(len(x) - 1):
            if (x[y] in 'ПРБЛ') and (x[y + 1] in 'ПРБЛ') or (x[y] in 'АО') and (x[y + 1] in 'АО'):
                return 0
        v.append(x)
        return 1
    return 0


s = 'ПАРАБОЛА'
v = []
for i in s:
    for j in s:
        for k in s:
            for o in s:
                for q in s:
                    for w in s:
                        for e in s:
                            for r in s:
                                func(str(i + j + k + o + q + w + e + r), v)

print(len(set(v)))
