f = open('17-1.txt')
arr = []
minimum = 10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)

vec = []
for i in range(1, len(arr)-1):
    if arr[i-1] > arr[i] and arr[i] < arr[i+1]:
        vec.append(arr[i])


print(len(vec), max(vec))