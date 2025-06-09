from itertools import product

s = '012345678'
counter = 0
for p in product(s, repeat=6):
    s = ''.join(p)
    if s[0] == '0' and s.count('4') == 1:
        s = 'X' + s.replace('0', 'X').replace('2', 'X').replace('6', 'X').replace('8', 'X') + 'X'
        if 'X4X' in s:
            counter += 1
print(counter)


