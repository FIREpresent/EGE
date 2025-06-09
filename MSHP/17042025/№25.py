from fnmatch import *
for x in range(0, 10**8+1, 2025):
    if fnmatch(str(x), '6*97*5'):
        print(x, x//2025)