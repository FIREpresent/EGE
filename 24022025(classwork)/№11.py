from itertools import *
s = "КОНФЕТА"
s = sorted(s)

count = 0

for x in product(s, repeat=5):
    st = ''.join(x)
    if st.count('Е') == 2 and st[1] != 'Ф':
        count += 1

print(count)