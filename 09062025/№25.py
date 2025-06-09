from fnmatch import *

for x in range(0, 10**12, 84318):
    if fnmatch(str(x), '5*7?') and len(set(list(str(x)))) == len(list(str(x))):
        print(x, x//84318)
