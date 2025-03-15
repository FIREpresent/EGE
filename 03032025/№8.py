from itertools import *

count = 0

for var in product(sorted('БОРИС'), repeat=6):
    num = ''.join(var)
    if num.count('Б') == 1 and num.count('Р') == 1 and num.count('С') <= 1:
        count += 1

print(count)
