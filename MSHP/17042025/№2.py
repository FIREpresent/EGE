from itertools import *

def f(x, y, z, w):
    return ((x <= y) and (y <= w)) or (z == (x or y))

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    tab = [(1, a1, a2, 1), (1, a3, a4, a5), (a6, 1, a7, 1)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(p)