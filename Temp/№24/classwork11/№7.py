with open('24-7.txt', 'r') as file:
    s = file.read().strip()

max_len = 0
current_start = 0
state = 'start'  # Состояния: 'start', 'number', 'after_op', 'zero'
number_start = 0

for i in range(len(s)):
    char = s[i]

    # Недопустимый символ
    if char not in '0123456789+*':
        current_start = i + 1
        state = 'start'
        continue

    # Обработка состояний
    if state == 'start':
        if char == '0':
            state = 'zero'
            current_start = i
            max_len = max(max_len, 1)
        elif char in '123456789':
            state = 'number'
            number_start = i
            current_start = i
        elif char in '+*':
            current_start = i + 1
        continue

    elif state == 'number':
        if char in '+*':
            state = 'after_op'
        elif char == '0':
            pass  # Валидная часть числа (например, 10)
        else:
            # Проверка ведущего нуля
            if s[number_start] == '0':
                current_start = number_start + 1
                state = 'start'
                # Повторная обработка текущего символа
                i -= 1
        # Обновление длины, если состояние 'number'
        max_len = max(max_len, i - current_start + 1)

    elif state == 'after_op':
        if char in '123456789':
            state = 'number'
            number_start = i
        elif char == '0':
            current_start = i + 1
            state = 'start'
        else:
            current_start = i + 1
            state = 'start'
        # Если переход в 'number', обновить длину
        if state == 'number':
            max_len = max(max_len, i - current_start + 1)

    elif state == 'zero':
        if char in '+*':
            current_start = i + 1
            state = 'start'
        else:
            current_start = i + 1
            state = 'start'

print(max_len)