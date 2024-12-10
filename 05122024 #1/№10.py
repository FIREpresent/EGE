# from itertools import *
# def func1(arr):
#     for x in permutations(arr):
#         if x[0] + x[1] == x[2] + x[3]:
#             return 1
#     return 0
#
# f = open('1_9.csv')
# lines = f.readlines()
# count = 0
# for line in lines:
#     line = list(map(int, line.strip().split(';')))
#     if func1(line) and (max(line) < sum(line) - max(line)):
#         count += 1
# f.close()
# print(count)
# count = 7
# n = 1
# t = 7
# while n < 9:
#     n += t
#     t += 1
#     count += 1
#
# print(n, t-1, count-1)



# for p in range(2, 1001):
#     for q in range(3, 1001):
#         if p != q:
#             if p**3 + 392*p == q**3 - 64*q:
#                 print(p, q, p*q)
#                 break

print(sum([i for i in range(1, 41)]))