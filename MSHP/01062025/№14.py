alph = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
alph = sorted(alph)
alph = alph[:21]

for x in alph[::-1]:
    if (int(f'8G{x}I2', 21) + int(f'6EI{x}FC3', 21) + int(f'455E{x}', 21) + int(f'D5H{x}95596', 21) + int(f'KE7{x}', 21) + int(f'8CG{x}33E6', 21)) % 20 == 0:
        print((int(f'8G{x}I2', 21) + int(f'6EI{x}FC3', 21) + int(f'455E{x}', 21) + int(f'D5H{x}95596', 21) + int(f'KE7{x}', 21) + int(f'8CG{x}33E6', 21)) // 20)
        break
