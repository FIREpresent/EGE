# file = open('17.txt')
# f = file.readlines()
# v = []
# for x in f:
#     v.append(int(x.strip()))
#
# maximum = -1
# count = 0
# for i in range(len(v)-1):
#     for j in range(i+1, len(v)):
#         if (v[i] + v[j]) % 2 != 0 and (v[i] * v[j]) % 5 == 0:
#             count += 1
#             maximum = max(maximum, v[i] + v[j])
# print(count, maximum)

from itertools import *

file = open('17.txt')
f = file.readlines()
v = []
for x in f:
     v.append(int(x.strip()))

maximum = -1
count = 0
c = combinations(v, r=2)
for x, y in c:
     if (x + y) % 2 != 0 and (x * y) % 5 == 0:
         count += 1
         maximum = max(maximum, x+y)
print(count, maximum)

# file = open('17.txt')
# f = file.readlines()
# vec_chet_del1 = []
# vec_nechet_del1 = []
#
# vec_chet_nedel_2 = []
# vec_nechet_nedel2= []
#
# for x in f:
#     num = int(x.strip())
#     if num % 2 == 0 and num % 5 == 0:
#         vec_chet_del1.append(num)
#     elif num % 2 != 0 and x % 5 == 0:
#         vec_nechet_del1.append(num)
#     elif num % 2 == 0 and num % 5 != 0:
#         vec_chet_nedel_2.append(num)
#     else:
#         vec_nechet_nedel2.append(num)
#
# maximum = -1
# count = 0
# for
# print(count, maximum)

