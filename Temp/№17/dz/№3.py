
f = open('17-1.txt')

nums = list(map(int, f.readlines()))
pair_count, max_n = 0, -float('Inf')

for i in range(1, len(nums)):
    if (nums[i-1] % 9 == 0 and nums[i] % 9 != 0 and abs(nums[i]) % 8 == 3) or (nums[i-1] % 9 == 0 and nums[i] % 9 != 0 and abs(nums[i-1]) % 8 == 3):
        pair_count += 1
        max_n = max(max_n, nums[i-1], nums[i])

print(pair_count, max_n)