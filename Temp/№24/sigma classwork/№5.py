from re import *

s = open('24-5 (4).txt').read()

src = r'AF(0|[1-9][0-9]*)([*+](0|[1-9][0-9]*))*'

sp = [x.group() for x in finditer(src, s)]
mx_s = max(sp, key=len)

print(len(mx_s))