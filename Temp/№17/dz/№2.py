def func(num, d):
    s = ''
    while num:
        s += str(num%d)
        num = num//d
    return s[::-1]

count = 0
maximum = 10**10
for elem in range(1529, 9483):
    if func(elem, 2)[-2] == '0' and func(elem, 2)[-1] == '1' and func(elem, 5)[-1] == '3':
        count += elem
        maximum = min(maximum, elem)

print(count, maximum)