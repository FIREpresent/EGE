from itertools import permutations
s1 = 'АБ АГ АЕ ГЕ ГБ БВ ВД ДЖ ЕЖ ЖИ ИВ'.split()
s2 = '15 17 18 24 27 28 34 35 37 47 56 68 x'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7 8')
for x in permutations('АБВГДЕЖИ'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)