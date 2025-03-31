f = open('17.txt')
arr = []
maximum = -10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)

count = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if abs(arr[i] - arr[j]) % 36 == 0 and (arr[i] % 13 == 0 or arr[j] % 13 == 0):
            count += 1
            maximum = max(maximum, abs(arr[i] - arr[j]))
print(count, maximum)
