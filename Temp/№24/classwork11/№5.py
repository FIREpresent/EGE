with open('24-5.txt', 'r') as file:
    s = file.read().strip()

max_count = 0
current_count = 0
n = len(s)

for i in range(0, n - 2, 3):
    a, b, c = s[i], s[i+1], s[i+2]
    if a.isdigit() and b.isdigit() and c in {'A', 'B', 'C'}:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

print("Задача 24-5:")
print(max_count)