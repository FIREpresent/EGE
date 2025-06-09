from itertools import *

count = 0
i = 0
for var in product(sorted('ТИМОФЕЙ'), repeat=6):
    i += 1
    num = ''.join(var)
    if num.count('И') + num.count('О') + num.count('Е') == num.count('Т') + num.count('М') + num.count('Ф') + num.count('Й'):
        count += 1
print(count)

