f = open('24.txt').readline()

dic = dict()
for i in range(1, len(f)-1):
    # print(f[i-1], f[i], f[i+1])
    if f[i-1] == f[i+1]:
        dic[f[i]] = dic.get(f[i], 0) + 1

print(dic)