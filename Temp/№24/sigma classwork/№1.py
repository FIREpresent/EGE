f = open('24-1 (11).txt')
s = f.read()
alph = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
alph = sorted(alph)
alph = alph[:16]

v = []
summ = ''
for a in s:
    if a in alph:
        summ += a
    else:
        v.append(summ)
        summ = ''
print(len(sorted(v, key= lambda x: len(x), reverse=True)[0]))