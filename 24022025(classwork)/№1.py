from itertools import permutations
s1 = 'АБ АГ БВ ВГ ВЕ ГЖ ГД ДЕ ЕЖ ЕК ЖИ ИК'.split()
s2 = '12 18 24 26 27 35 39 49 57 68 69 79'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7 8 9')
for x in permutations('АБВГДЕЖИК'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)

# АГ 21
# ГД 12

#значит второй вариант: 16
