from fnmatch import *
for i in range(0, 10**8 + 1, 161):
    if fnmatch(str(i), '12*4?65'):
        print(i, i // 161)