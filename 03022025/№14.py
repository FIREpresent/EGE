s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = s[:15]
for x in s:
    for y in s:
        if (int(f'90{x}4{y}', 15) + int(f'91{x}{y}2', 16)) % 56 == 0:
            print((int(f'90{x}4{y}', 15) + int(f'91{x}{y}2', 16)) // 56)
            break