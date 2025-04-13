with open('24-3.txt', 'r') as file:
    s = file.read().strip()

max_length = 0
current_points = 0
left = 0

for right in range(len(s)):
    if s[right] == '.':
        current_points += 1

    # Если точек больше 4, сужаем окно слева
    while current_points > 4:
        if s[left] == '.':
            current_points -= 1
        left += 1

    # Обновляем максимальную длину
    current_length = right - left + 1
    if current_length > max_length:
        max_length = current_length

print(max_length)