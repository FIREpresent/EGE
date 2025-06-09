from itertools import *

count = 0
i = 0
for var in permutations(sorted('ХОЧУНАБЮДЖЕТ'), r=12):
    i += 1
    num = ''.join(var)
    num = num.replace('А', 'X').replace('О', 'X').replace('У', 'X').replace('Е', 'X').replace('Ю', 'X')
    if 'XXXXX' in num:
        count += 1
        print(count)

print(12*11*10*9*8*7*6*5*4*3*2*1 - count)
