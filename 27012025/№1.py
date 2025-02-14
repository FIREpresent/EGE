from itertools import permutations
s1 = 'АБ АГ АЕ ЕГ ЕЖ БВ ВД ВК ГД ДК ЖИ ИК'.split()
s2 = '15 16 26 27 29 35 37 38 48 49 58 67'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7 8 9')
for x in permutations('АБВГДЕЖИК'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)