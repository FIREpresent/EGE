s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = sorted(s)

s = s[:21]
for x in s:
    if (int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)) % 20 == 0:
        print((int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)) // 20)
        break