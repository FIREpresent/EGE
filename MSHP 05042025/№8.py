from itertools import product

s = 'МЕЧТА'
count = 0
for p in product(s, repeat=6):
    s = ''.join(p)
    if s.count('А') >= 3:
        count += 1

print(count)


