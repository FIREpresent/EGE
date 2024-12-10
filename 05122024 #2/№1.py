from itertools import permutations
s1 = 'BH BA HF FD FG AE EG EC GC CD'.split()
s2 = '12 14 17 24 28 35 37 38 46 58 67'
s2 += ' ' + s2[::-1]
print('1 2 3 4 5 6 7 8')
for x in permutations('ABCDEFGH'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        print(*x)
# 8 + 30 = 38