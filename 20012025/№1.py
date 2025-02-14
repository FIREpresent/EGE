from itertools import permutations
s1 = 'BD BC BE CH ED EH DG HF FG FA GA'.split()
s2 = '12 13 14 25 27 34 37 48 56 58 68'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7 8')
for x in permutations('ABCDEFGH'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)

#7 + 4 = 11