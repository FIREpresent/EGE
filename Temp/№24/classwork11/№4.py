with open('24-4.txt', 'r') as file:
    s = file.read().strip()

max_count = 0
current_count = 0
n = len(s)

for i in range(0, n - 2, 3):
    triplet = s[i:i+3]
    if triplet in {'NPO', 'PNO'}:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

print("Задача 24-4:")
print(max_count)