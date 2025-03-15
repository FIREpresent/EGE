from itertools import *
s = "ПАРУС"
s = sorted(s)
v = []
count = 0
i = 0
for x in product(s, repeat=5):
    i += 1
    st = ''.join(x)

    if st.count('У') <= 1 and "АА" not in st:
        v.append([st, i])
        #print(i)
        # count += 1

print(v)
# print(count)