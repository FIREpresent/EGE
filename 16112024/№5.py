v = []
for n in range (456789012, 400000000, -1):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '11'
    else:
        s = '1' + s + '10'
    num = int (s, 2)
    v.append(num)
print(max(num))