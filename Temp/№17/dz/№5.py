f = open('17-3.txt')
arr = []
maximum = 10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)

maximum = 10**10
count = 0
for i in range(len(arr)-1):
    if (abs(arr[i] + arr[i+1])/2) % 7 == 0 and abs(arr[i] * arr[i+1]) % 2 != 0:
        count += 1
        maximum = min(maximum, (arr[i] + arr[i+1])//2)
print(count, maximum)