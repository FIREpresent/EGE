from itertools import *

def f(x, y, z, w):
    return (w <= z) and ((y <= x) == (z <= y))

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    tab = [(1, a1, a2, 0), (a3, 0, 1, a4), (1, 0, 0, 1)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [1, 1, 1]:
                print(*p)