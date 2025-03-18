f = open('17-3.txt')
arr = []
maximum = -10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)

count = 0
for i in range(len(arr)-1):
    if (abs(arr[i]) % 2 == 0 and abs(arr[i+1]) % 2 != 0 and abs(arr[i]) % 4 == 0 and abs(arr[i+1]) % 11 == 0) or (abs(arr[i+1]) % 2 == 0 and abs(arr[i]) % 2 != 0 and abs(arr[i+1]) % 4 == 0 and abs(arr[i]) % 11 == 0):
        count += 1
        maximum = max(maximum, arr[i] + arr[i+1])

print(count, maximum)
