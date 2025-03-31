from itertools import permutations
s1 = 'АБ АВ АГ ВЕ БД БГ ДГ ДК ЕГ ЕК КЛ'.split()
s2 = '14 18 23 26 28 45 47 56 57 67 78'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7 8')
for x in permutations('АБВГДЕКЛ'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)