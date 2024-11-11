from itertools import *

# v = sorted('M,A,Н,Г,У,С,T'.split(','))
# print(v)
i = 0
s = []
for p in product(sorted("МАНГУСТ"), repeat=6):
    i += 1
    # print(i, a)
    if p.count("М") == 2 and p[0] != "У" and p.count("Г") <= 1:
        s.append(i)

print(max(s))
