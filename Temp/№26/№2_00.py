file = open("26-2.txt")
V, K, N = map(int, file.readline().split())

array = []
for i in range(N):
    array.append(int(file.readline()))
array.sort(reverse=True)

array_disks = [0] * K
local_folder = []
disk_num = 0
for i in range(N):
    for j in range(disk_num, disk_num + K):
        if array_disks[j % K] + array[i] <= V:
            array_disks[j % K] += array[i]
            disk_num = j + 1
            break
    else:
        local_folder.append(array[i])

print(sum(local_folder), len(local_folder))