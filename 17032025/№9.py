def visible(num, arr):
    return num > sum(arr)/len(arr)

def func(arr, vec):
    c = 0
    for elem in arr:
        if visible(elem, vec):
            c += 1
    return c


with open('9.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        a = [el for el in l if el % 2 == 0]
        b = [el for el in l if el % 2 != 0]
        if func(a, l) > func(b, l) and sum(a) < sum(b):
            count += 1

    print(count)