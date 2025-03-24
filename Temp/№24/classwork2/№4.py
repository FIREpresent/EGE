with open('24-4.txt', 'r') as file:
    count = 0
    for line in file:
        k_count = line.count('K')
        u_count = line.count('U')
        if k_count > u_count:
            count += 1
print(count)