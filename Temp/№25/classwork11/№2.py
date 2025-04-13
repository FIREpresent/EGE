from fnmatch import fnmatch

for i in range(0, 10**10 + 1, 9601):
    if fnmatch(str(i), '19*105*9'):
        print(i, i // 9601)