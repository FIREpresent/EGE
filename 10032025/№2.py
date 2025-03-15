from itertools import *

def f(x, y, z, w):
    return (((not(x)) or z) == (y and (not(w)))) <= (z and y)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(a1, 1, 1, 1), (a2, a3, 1, 1), (a4, a5, 1, a6)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(*p)