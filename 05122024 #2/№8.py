from itertools import *
string1 = '0246'
string2 = '357'
count = 0

for var in product(string1[1:], string2, string1, string2, string1):
    num = ''.join(var)
    num = list(num)
    if len(set(num)) == len(num):
        count += 1

for var in product(string2, string1, string2, string1, string2):
    num = ''.join(var)
    num = list(num)
    if len(set(num)) == len(num):
        count += 1

print(count)