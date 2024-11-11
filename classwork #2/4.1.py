from itertools import *

v = sorted('А,Б,З,И'.split(','))
print(v)
i = 0
for a in product(v, repeat = 4):
    i += 1
    if a == ('И', 'З', 'Б', 'А'):
        print(i, a)
        break