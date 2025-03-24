# with open('24-2.txt') as f:
#     s = f.readline()
#
#     l = s.split('T')
#
#     max_ = 0
#     b = 100
#
#     for i in range(len(l) - b):
#         str_ = 'T'.join(l[i : i + b + 1])
#         max_ = max(max_, len(str_))
# print(max_)

s = 'TTTTVZTTZTTTTZ'
l = s.split('T')
print(l)
str_ = 'T'.join(l[0 : 0 + 10 + 1])
print(str_)