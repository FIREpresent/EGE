alph = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
alph = sorted(alph)
alph = alph[:17]

for x in alph[::-1]:
    if (int(f'819{x}6{x}32', 17) + int(f'45656925{x}', 17) + int(f'771377{x}1', 17)) % 16 == 0:
        print((int(f'819{x}6{x}32', 17) + int(f'45656925{x}', 17) + int(f'771377{x}1', 17)) // 16)