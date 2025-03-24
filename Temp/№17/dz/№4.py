f = open('17-2.txt')
arr = []
minimum = 10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)
    minimum = min(num, minimum)

maximum = -10**10
count = 0
for i in range(len(arr)-1):
    if abs(arr[i] + arr[i+1]) % 3 == 0 and abs(arr[i] + arr[i+1]) % 6 != 0 and abs(arr[i] * arr[i+1]) % 10 == 8:
        count += 1
        maximum = max(maximum, arr[i] + arr[i+1])
print(count, maximum)
