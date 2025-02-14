f = open('zadanie24_1.txt').readline()
counter = 0
maximum = 0
for i in range(len(f)):
    if (counter % 2 == 0 and f[i] == 'A') or (counter % 2 == 1 and f[i] == 'B'):
        counter += 1
        maximum = max(maximum, counter)
    elif f[i] == 'A':
        counter = 1
    else:
        counter = 0
print(maximum)