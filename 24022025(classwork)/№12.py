from itertools import *
s = "ЯРОСЛАВ"
s = sorted(s)

count = 0

for x in permutations(s, r=5):
    st = ''.join(x)
    st = st.replace("Я", "X").replace("О", "X").replace("А", "X")
    st = st.replace("Р", "Y").replace("С", "Y").replace("Л", "Y").replace("В", "Y")
    if 'XX' not in st and st.count('Y') > st.count('X'):
        count += 1

print(count)