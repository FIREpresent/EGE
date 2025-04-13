alph = sorted('0123456789QWERTYUIOPASDFGHJKZXCVBNM')[:16]

for x in alph[::-1]:
    if (int(f'3BB{x}8', 16) + int(f'B67A{x}FE62', 16) + int(f'BEA2{x}D49B', 16) + int(f'8D7D{x}', 16)) % 15 == 0:
        print(int(f'3BB{x}8', 16) + int(f'B67A{x}FE62', 16) + int(f'BEA2{x}D49B', 16) + int(f'8D7D{x}', 16) // 15)
        break