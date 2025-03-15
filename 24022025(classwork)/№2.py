from itertools import permutations
s1 = 'AC AD AG CD GD DB DE EF BF'.split()
s2 = '13 17 25 27 34 37 47 56 67'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7')
for x in permutations('ABCDEFG'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)