f = open('17.txt')
vec = [int(i) for i in f]

count = 0
minimum_sum, minimum = 10**10, 10**10

for i in range(len(vec)):
    if len(str(vec[i])) == 3 and vec[i] % 10 == 5:
        minimum = min(minimum, vec[i])

for i in range(len(vec) - 1):
    if (len(str(vec[i])) != len(str(vec[i + 1]))) and ((len(str(vec[i])) == 3) or (len(str(vec[i + 1])) == 3)) and ((vec[i] + vec[i + 1]) % minimum == 0):
        minimum_sum = min(minimum_sum, (vec[i] + vec[i + 1]))
        count += 1
print(count, minimum_sum)
