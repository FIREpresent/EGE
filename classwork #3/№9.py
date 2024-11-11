def func(arr):
    if (int(arr[0]) * int(arr[1]) + int(arr[2]) * int(arr[1]) < int(arr[2])*int(arr[0]))  or (int(arr[0]) * int(arr[1]) + int(arr[0]) * int(arr[2]) < int(arr[2])*int(arr[1]))  or (int(arr[2]) * int(arr[1]) + int(arr[2]) * int(arr[0]) < int(arr[0])*int(arr[1])):
        return 1
    return 0

f = open('09.csv', 'r')
lines = f.readlines()
count = 0
for line in lines:
    count += func(sorted(line.strip().split(',')))
f.close()
print(count)