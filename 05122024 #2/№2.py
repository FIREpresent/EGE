from itertools import *

def f(x, y, z, w):
    return ((x == y) <= (not(z) or w)) == (not(((w <= x) or (y <= z))))

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(0, 1, a1, a2), (a3, a4, 1, 0), (0, a5, 0, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [1, 1, 1]:
                print(p)