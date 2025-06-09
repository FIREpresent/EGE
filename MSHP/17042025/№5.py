a = []
for n in range(100000, 1, -1):
    s = bin(n)[2:]
    s = str(s)
    if s.count('1') % 4 == 0:
        s = "10" + s
    else:
        s = "11" + s

    if int(s, 2) % 2 != 0:
        s = s + '0'
    else:
        s = s + '1'

    r = int(s, 2)
    if r <= 250:
        print(n)
        break
