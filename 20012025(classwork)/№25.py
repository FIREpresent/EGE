from fnmatch import fnmatch

for x in range(0, 10**10, 3023):
    if fnmatch(str(x), '1?954*21'):
        print(x, x // 3023)