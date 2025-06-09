from itertools import *

def f(x, y, z, w):
    return (y <= (not (x <= z))) or w

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    tab = [(a1, 0, a2, a3), (0, 1, a4, a5), (1, a6, a7, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(p)