from itertools import *

def f(x, y, z, w):
    return ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x)))

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(1, a1, 1, 1), (a2, 0, 0, 0), (a3, a4, 0, a5)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(p)