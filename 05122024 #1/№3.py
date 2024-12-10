from itertools import *

def f(x, y, z, w):
    return (not(x <= z)) or (y == w) or y

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    tab = [(1, 0, a1, a2), (a3, 1, 0, a4), (0, a5, a6, a7)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(p)