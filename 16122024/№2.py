from itertools import *

def f(x, y, z, w):
    return (x or (not(y))) <= (w == z)

def f2(x, y, z, w):
    return (x or (not(y))) == (w <= z)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(0, a1, 0, 0), (a2, 1, 1, a3), (a4, 0, 0, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, a5] and [f2(**dict(zip(p, r))) for r in tab] == [0, a6, 0]:
                print(p)