from re import *

s = open('24-4 (3).txt').read()

n = r'([1-9][0-9]*|0)'
mult = rf'(({n}\*)*0(\*{n})*)'
src = rf'({mult}(\+{mult})*)'

sp = [x.group() for x in finditer(src, s)]

rez=max(sp, key=len)

print(len(rez))