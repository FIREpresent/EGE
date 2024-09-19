s = '0123456789ABCDEFGH'
s = s[::-1]

for x in s:
    d = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if d % 18 == 0:
        print(d // 18)
        break
