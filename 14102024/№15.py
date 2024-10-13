from itertools import product
v = []
m = 0

for i in product('12', repeat = 13):
    i = str(''.join(i))
    if i.count('1') == 10 and i.count('2') == 3:
        if not(i in v):
            v.append(i)

for x in v:
    s = str(x)
    while '11' in s:
        if '112' in s:
            s = s.replace('112', '6', 1)
        else:
            s = s.replace('11', '3', 1)
    m = max(sum(list(map(int, list(s)))), m)
print(m)