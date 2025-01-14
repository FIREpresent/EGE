from itertools import *
s = '0123456789ABCDE'
counter = 0
for num in product(s[1:],s,s,s, s, s, s, s):
    num = ''.join(num)
    if num[0] != 0:
        if num.count('0') == 2 and sum([num.count('A'), num.count('B'), num.count('C'), num.count('D'), num.count('E')]) <= 4:
            counter += 1
            print(num)
print(counter)