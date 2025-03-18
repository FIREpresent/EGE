f = open('17-2.txt')
arr = []
minimum = 10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)

count = 0
for i in range(len(arr)-1):
    if arr[i] * arr[i+1] > 0 and (arr[i] + arr[i+1]) % 7 == 0:
        count += 1
        minimum = min(minimum, arr[i] * arr[i+1])
print(count, minimum)
