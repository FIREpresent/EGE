from itertools import *
s = "ОЛЬГА"
s = sorted(s)

count = 0
i = 0
for x in product(s, repeat=5):
    i += 1
    st = ''.join(x)

    if 'ОЛЬГА' in st:
        print(i)
        # count += 1

# print(count)