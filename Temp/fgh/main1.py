from re import *
# s = 'ABCDEABABABDBABCBEBDBABCBDBEBABC'
# pat = r'(?:[ABCE]*)'
# print(findall(pat, s))

s = 'ABCDEABABABDBABCBEBDBABCBDBEBABC'
pat = r'(?:[ABC]+)'
print(findall(pat, s))