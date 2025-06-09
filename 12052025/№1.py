from itertools import permutations
s1 = 'GE GB EC EF BC BA CD DF DA FA'.split()
s2 = '14 15 17 25 26 27 34 35 46 67'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7 8')
for x in permutations('ABCDEFG'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)