from fnmatch import *
for x in range(0, 10**10, 4173):
    if fnmatch(str(x), '1?2655*8'):
        print(x)