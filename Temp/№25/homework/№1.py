from fnmatch import *
for i in range(0, 10**8 + 1, 2023):
    if fnmatch(str(i), '3?1*57'):
        print(i, i // 2023)