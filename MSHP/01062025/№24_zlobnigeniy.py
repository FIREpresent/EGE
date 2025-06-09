# s = 'ABCDEABDDEABCCBADEABOBABEBRADE'
f = open('24.txt')
s = f.readline()
s = s.replace('DE', ' ')
v = s.split(' ')
arr = []
for i in range(len(v)-240):
    summ = v[i]
    for j in range(i+1, i+241):
        summ += 'DE' + v[j]
    summ += 'D'
    if i > 0:
        summ = 'E' + summ
    arr.append(summ)

print(arr)
print(len(max(arr, key=lambda x: len(x))))
