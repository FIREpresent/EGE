def conv(n):
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''
    while n:
        s = alph[n % 7] + s
        n //= 7
    return s

n = 343**1515 - 6*49**1520 + 5*49**1510 - 3*7**1530 - 1550
print(conv(n).count('0'))