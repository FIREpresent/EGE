def check(x):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] == x[j]:
                return 0
    return 1

def func(x):
    if (max(x)+min(x))/2 > (sum(x)-max(x)-min(x))/4 and check(x):
        return 1
    return 0

f = open("091.csv")
lines = f.readlines()
count = 0
for line in lines:
    count += func(list(map(int, line.strip().split(','))))
f.close()
print(count)