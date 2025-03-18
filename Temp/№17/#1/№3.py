f = open('17-1.txt')
arr = []
minimum = 10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)

count = 0
for i in range(len(arr)-1):
    if (abs(arr[i]) % 3 == 0 and abs(arr[i])%10 == 6) or (abs(arr[i+1]) % 3 == 0 and abs(arr[i+1])%10 == 6):
        count += 1
        minimum = min(minimum, arr[i], arr[i+1])

print(count, minimum)
