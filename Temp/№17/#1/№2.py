def func(num, d):
    s = ''
    while num:
        s += str(num%d)
        num = num//d
    return s[::-1]

count = 0
maximum = -10**10
for elem in range(3439, 7411):
    if func(elem, 2)[-1] != func(elem, 6)[-1] and (elem % 9 == 0 or elem % 10 == 0 or elem % 11 == 0):
        count += 1
        maximum = max(maximum, elem)

print(count, maximum)