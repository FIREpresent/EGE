f = open('17.txt')
count = 0
v = []
nums = [int(i) for i in f]
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) % 126 == 0:
            v.append(nums[i] + nums[j])
f.close()
print(len(v), max(v))
