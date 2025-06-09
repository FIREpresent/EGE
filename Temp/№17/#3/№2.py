a = [int(elem) for elem in open('17-2 (3).txt')]
max_el = -10**10
counter = 0
max_sum = -10**10

for elem in a:
    if len(str(abs(elem))) == 2:
        max_el = max(max_el, elem)

for i in range(len(a)-1):
    if (len(str(abs(a[i]))) == 2 or len(str(abs(a[i+1]))) == 2) and a[i]+a[i+1] <= max_el:
        counter += 1
        max_sum = max(max_sum, a[i]+a[i+1])
print(counter, max_sum)
