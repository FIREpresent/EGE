
f = open('18.txt')

nums = [int(i) for i in f]
maximum = 0
minimum = 10**10
l = len(nums)

for i in range(l):
    if nums[i] % 100 == 24:
        maximum = max(nums[i], maximum)

count = 0
for i in range(l - 2):
    c = 0
    v = [nums[i], nums[i+1],  nums[i+2]]

    for n in v:
        if 99 < n < 1000:
            c += 1

    if maximum < sum(v) and c == 1:
        count += 1
        minimum = min(nums[i] + nums[i+1] + nums[i+2], minimum)

f.close()
print(count, minimum)