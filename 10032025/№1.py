from itertools import permutations
s1 = 'АБ БВ БЕ БЖ ВЖ ЕЖ ЕД ДГ ДЖ ГЖ'.split()
s2 = '12 14 15 16 17 24 26 35 56 57'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7')
for x in permutations('АБВГДЕЖ'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)