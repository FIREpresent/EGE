from itertools import product
count = 0
sp = []
id = 1
is_p = 0
for s in product(sorted("КОМПЬЮТЕР"), repeat = 5):
    count += 1
    if s[0] != 'Ь' and s.count("К") == 2 and id % 2 != 0:
        id_p = id
    id += 1
print(id_p)