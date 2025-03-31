with open('24.txt') as file:
    count = 0
    for line in file:
        if line.count('E') > line.count('A'):
            count += 1
print(count)