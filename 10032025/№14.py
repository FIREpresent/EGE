s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = s[:9]
for A in range(1, 1000):
    flag = 1
    for x in s:
        if (int(f'842{x}5', 9) + A) % int(f'8{x}725', 9) == 0:
            flag = 0
            break
    if flag == 0:
        print(A)
        break