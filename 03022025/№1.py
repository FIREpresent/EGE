from itertools import permutations
s1 = 'АВ АГ АБ БГ ВГ ВД ВЕ ДЕ ДГ ДК ЕК ГК'.split()
s2 = '12 14 16 23 24 25 27 35 37 46 47 67'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7 8')
for x in permutations('АБВГДЕИК'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)