from itertools import *


def f(x, y, z, w):
    return (w == (z <= x)) and y

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(a1, 0, a2, 0), (1, a3, 1, 1), (a4, a5, 0, 0)]
    if len(set(tab)) == len(tab):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [1, 0, 1]:
                print(*p, sep='')