from itertools import permutations
s1 = 'CF CD FB DA DE EA EG GA GB BA'.split()
s2 = '13 16 24 25 26 27 37 45 47 56'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7')
for x in permutations('ABCDEFG'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)