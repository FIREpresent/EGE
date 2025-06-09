from itertools import *
def f(x, y, z, w):
    return (x <= y) and (y <= z) and (z <= w)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(a1, 0, 1, a2), (a3, 1, a4, 0), (a5, 0, 1, a6)]
    if len(set(tab)) == len(tab):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [1, 1, 1]:
                print(p)

