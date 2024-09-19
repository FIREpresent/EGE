

def func(x):
    if (x.count(min(x)) == 1) and (len(x) != len(set(x))) and (max(x) > ((sum(x[i] for i in range(len(x)))-max(x)) / 5)*3):
        return 1
    return 0

f = open("091.csv")
lines = f.readlines()
count = 0
for line in lines:
    count += func(list(map(int, line.strip().split(','))))
f.close()
print(count)
