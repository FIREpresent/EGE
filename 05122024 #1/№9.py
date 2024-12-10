
from itertools import *

# count = 0
# for var in product('12345678', repeat = 11):
#     num = ''.join(var)
#     num = list(num)
#     if num.count('1') < 4 and num.count('2') < 4 and num.count('3') < 4 and num.count('4') < 4 and num.count('5') < 4 and num.count('6') < 4 and num.count('7') < 4 and num.count('8') > 4:
#         for i in range(len(num)):
#             if int(num[i]) % 2 == 0:
#                 num[i] = 'X'
#             else:
#                 num[i] = 'Y'
#         if 'XX' not in num and 'YY' not in num:
#             count += 1
# print(count)

string1 = '2468'
string2 = '1357'
count = 0

for var in product(string1, string2, string1, string2, string1, string2, string1, string2, string1, string2, string1):
    num = ''.join(var)
    num = list(num)
    if num.count('1') <= 4 and num.count('2') <= 4 and num.count('3') <= 4 and num.count('4') <= 4 and num.count('5') <= 4 and num.count('6') <= 4 and num.count('7') <= 4 and num.count('8') < 4:
        count += 1

for var in product(string2, string1, string2, string1, string2, string1, string2, string1, string2, string1, string2):
    num = ''.join(var)
    num = list(num)
    if num.count('1') <= 4 and num.count('2') <= 4 and num.count('3') <= 4 and num.count('4') <= 4 and num.count('5') <= 4 and num.count('6') <= 4 and num.count('7') <= 4 and num.count('8') < 4:
        count += 1

print(count)