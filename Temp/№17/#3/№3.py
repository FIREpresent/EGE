a = [int(elem) for elem in open('17-3 (3).txt')]
summ = sum(elem for elem in a if elem < 0)
counter = 0
max_sum = -10**10
for i in range(len(a)-2):
    if max(a[i], a[i+1], a[i+2]) * min(a[i], a[i+1], a[i+2]) > summ:
        counter += 1
        max_sum = max(max_sum, a[i] + a[i+1] + a[i+2])

print(counter, max_sum)