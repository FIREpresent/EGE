def func(arr):
    if int(arr[0]) + int(arr[1]) < int(arr[2]) or int(arr[0]) + int(arr[1]) < int(arr[3]):
        return 1
    return 0

f = open('107_9.csv', 'r')
lines = f.readlines()
count = 0
for line in lines:
    count += func(sorted(line.strip().split(',')))
f.close()
print(count)