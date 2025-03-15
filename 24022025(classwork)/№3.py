from itertools import permutations
s1 = 'AE AH ED EB DB BG GH GF HC FC'.split()
s2 = '12 18 25 28 34 36 46 57 67 78'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7 8')
for x in permutations('ABCDEFGH'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)