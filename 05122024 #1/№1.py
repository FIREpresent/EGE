from itertools import permutations
s1 = 'AB AG BC BD GF GC FC FE EC ED DC'.split()
s2 = '13 14 16 25 27 34 35 45 46 47 67'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7')
for x in permutations('ABCDEFG'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)