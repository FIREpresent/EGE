def func(num, d):
    s = ''
    while num:
        s += str(num%d)
        num = num//d
    return s[::-1]

count = 0
summ = 0
for elem in range(255, 4096):
    if (func(elem, 3).count('1') == 1 or func(elem, 3).count('0') == 2) and elem % 10 == 0 and elem % 20 != 0:
        count += 1
        summ += elem

print(count, summ)