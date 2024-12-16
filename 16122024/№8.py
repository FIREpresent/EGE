from itertools import *
string1 = '012345678'
count = 0

for var in product(string1, repeat=12):
    num = ''.join(var)
    num = list(map(int, num))
    if num[0] != 0:
        for i in range(11):
            if (((num[i]+num[i+1]) % 2 == 0) and (num[i+1] > num[i])) or (((num[i]+num[i+1]) % 2 != 0) and (num[i+1] < num[i])):
                count += 1

print(count)