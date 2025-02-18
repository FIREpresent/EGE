from itertools import *

count = 0

for var in product(sorted('АОУ', reverse=True), repeat=6):
    num = ''.join(var)
    count += 1
    if num == 'ОУУУОО':
        print(count)
        break
