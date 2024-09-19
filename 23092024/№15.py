s = '0123456789A'

for x in s:
    d = int(f'28{x}2', 18) + int(f'93{x}5', 12)
    if d % 133 == 0:
        print(d // 133)
        break