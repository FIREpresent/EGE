from fnmatch import fnmatch

num = 30120145
del_ = 1917
start = num - num % del_
end = 3912914995

for i in range(start, end + 1, del_):
    if fnmatch(str(i), '3?12?14*5'):
        print(i, i // del_)