from itertools import *
from time import *

def f(x, y, z, w):
    return ((x and not(y)) <= (not(z) or not(w))) and ((w <= x) or y)


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(1, a1, 1, 1), (0, a2, a3, 0), (1, a4, a5, a6)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(p)