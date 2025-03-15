from itertools import *


def f(x, y, z, w):
    return (x and y) or (y == z) or w


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(1, a1, a2, 0), (0, 1, a3, a4), (1, 0, a5, 1)]
    if len(set(tab)) == len(tab):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(p)
