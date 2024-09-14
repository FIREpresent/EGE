v = []
for a in '0123456':
    for b in '0123456':
        num1 = int(b + a + '320', 7)
        num2 = int('1' + a + '3' + b + '3', 9)
        if (num1 + num2) % 181 == 0:
            v.append((num1 + num2) / 181)
print(int(min(v)))