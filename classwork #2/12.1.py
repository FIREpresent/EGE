from itertools import *

count = 0
for a1, a2, a3, a4, a5 in product('01234567', repeat=5):
    s = a1+a2+a3+a4+a5
    if s.count('6') == 1 and s[0] != '0':
        if s.index('6') == 0 and int(s[s.index('6')+1]) % 2 == 0:
            count += 1
        elif s.index('6') == 4 and int(s[s.index('6')-1]) % 2 == 0:
            count += 1
        elif (0 < s.index('6') < 4) and (int(s[s.index('6')+1]) % 2 == 0 and int(s[s.index('6')-1]) % 2 == 0):
            count += 1

print(count)