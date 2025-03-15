f = open('24.txt').readline()
vec = f.split('F')
vec = vec[:-1]
count = 1 #так как удалили F
maximum = 0

for i in range(len(vec)):

    if vec[i].count('A') <= 2:
        count += len(vec[i]) + 1 #так как удалили F
        maximum = max(maximum, count)
    else:
        count = 1

print(maximum)