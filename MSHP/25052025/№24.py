with open('24-1.txt', 'r') as f:
    s = f.read().strip()

max_length = 0
current_start = -1
last_two = []

for i, c in enumerate(s):
    # Проверяем, является ли символ допустимым шестнадцатеричным
    if not (c.isdigit() or ('A' <= c <= 'F')):
        current_start = -1
        last_two = []
        continue

    # Если последовательность не начата
    if current_start == -1:
        if c == '0':
            continue  # Не может начаться с нуля
        else:
            current_start = i  # Начало новой последовательности
            last_two = [c]
    else:
        # Продолжаем последовательность
        last_two.append(c)
        # Оставляем только последние два символа
        if len(last_two) > 2:
            last_two = last_two[-2:]
        # Проверяем окончание на '00'
        if len(last_two) == 2 and last_two == ['0', '0']:
            current_len = i - current_start + 1
            if current_len > max_length:
                max_length = current_len

print(max_length)