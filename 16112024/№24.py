from fnmatch import fnmatch

for num in range(2024, 10 ** 10, 2024):
    if fnmatch(str(num), "1?2157*4"):
        print(num, num // 2024)
