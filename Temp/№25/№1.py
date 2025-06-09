from fnmatch import fnmatch

for i in range(0, 10**9+1, 31*2031):
    if i % 2031 == 0 and i % 31 == 0:
        if fnmatch(str(i), ''):
            print(i, i %)