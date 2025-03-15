s = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
s = sorted(s)
for x in s[:9]:
    for y in s[:9]:
        if (int(f'2{y}66{x}', 9) + int(f'{x}0{y}1', 12)) % 170 == 0:
            print((int(f'2{y}66{x}', 9) + int(f'{x}0{y}1', 12)) // 170)
            break