with open('24-6.txt', 'r') as file:
    s = file.read().strip()

vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
max_length = 0
left = 0
count = {v: 0 for v in vowels}

for right in range(len(s)):
    char = s[right]
    if char in vowels:
        count[char] += 1
        while count[char] > 8:
            if s[left] in vowels:
                count[s[left]] -= 1
            left += 1
    max_length = max(max_length, right - left + 1)

print("Задача 24-6:")
print(max_length)