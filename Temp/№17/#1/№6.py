f = open('17-3.txt')
arr = []
minimum = 10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)

count = 0
for i in range(len(arr)-2):
    a = abs(arr[i])
    b = abs(arr[i+1])
    c = abs(arr[i+2])
    if (a % 12 == 0 or b % 12 == 0 or c % 12 == 0) and a % 3 == 0 and b % 3 == 0 and c % 3 == 0:
        count += 1
        minimum = min(minimum, (arr[i] + arr[i+1] + arr[i+2]) // 3)

print(count, minimum)
