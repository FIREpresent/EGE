def conv(n):
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''
    while n:
        s = alph[n % 25] + s
        n //= 25
    return s

n = 13 * 625**1320 + 12 * 125**1230 - 14 * 25**1140 - 13 * 5**1050 - 2500
print(conv(n).count('0'))