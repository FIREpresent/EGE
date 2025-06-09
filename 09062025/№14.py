def f(x, base):
    alph = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    alph = sorted(alph)[:base]
    s = ''
    while x:
        s += alph[x % base]
        x //= base
    return s[::-1]


alph = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
alph = sorted(alph)[:7]
s = f(15 * 343 ** 2031 + 7 * 49 ** 1142 - 3 * 7 ** 111 + 7 ** 222 - 16809, 7)
for i in range(7):
    if i % 2 != 0:
        s = s.replace(alph[i], 'X')
    else:
        s = s.replace(alph[i], 'Y')

print(abs(s.count('Y') - s.count('X')))
