alph = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
alph = sorted(alph)
alph = alph[:15]

for x in alph[::-1]:
    if (int(f'67845{x}65', 15) + int(f'1{x}23456', 15)) % 14 == 0:
        print((int(f'67845{x}65', 15) + int(f'1{x}23456', 15)) // 14)