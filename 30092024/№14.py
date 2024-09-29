v = []
for x in '0123456789A':
    for y in '0123456789A':
        num = int(x + '341' + y, 11) + int('56' + x + '1' + y, 19)
        if num % 305 == 0:
            v.append(num//305)
print(min(v))