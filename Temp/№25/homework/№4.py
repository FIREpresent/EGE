from fnmatch import *
count = 0
for i in range(0, 10**10 + 1, 73):
    if fnmatch(str(i), '12345*76'):
        if count < 5:
            print(i, i // 73)
            count += 1
        else:
            break