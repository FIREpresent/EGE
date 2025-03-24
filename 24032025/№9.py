def func(arr, vec, temp):
    counter = 0
    for i in range(len(arr)):
        if (arr.count(arr[i]) == 1) and (temp[i].count(arr[i]) >= 336) and (arr[i] < (sum(arr)/len(arr))):
            counter += 1
    if counter == 1:
        return 1
    return 0


with open('9.csv') as f:
    count = 0
    v = []
    for line in f:
        l = list(map(int, line.split()))
        v.append(l)
    temp = []

    for i in range(len(l)):
        temp1 = []
        for j in range(len(v)):
            temp1.append(v[j][i])
        temp.append(temp1)


    for line in v:
        if func(line, v, temp):
            count += 1
    print(count)