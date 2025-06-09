from itertools import *

count = 0

for var in product(sorted('ЖАЛЕЙ'), repeat=5):
    num = ''.join(var)
    if num.count('Й') <= 1 and num[0] != 'Й' and num[-1] != 'Й' and 'ЕЙ' not in num and 'ЙЕ' not in num:
        count += 1

print(count)
