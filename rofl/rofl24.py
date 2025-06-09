import re

with open('24.txt', 'r') as file:
    content = file.read()

# Регулярное выражение, которое:
# 1. Исключает "AB" до первого и после последнего вхождения
# 2. Гарантирует ровно 100 "AB" внутри последовательности
pattern = r'''
(
    (?:(?!AB).)*        # Любые символы до блока (без AB)
    (?:AB               # Каждое AB
        (?:(?!AB).)*    # Любые символы между AB, кроме нового AB
    ){100}              # Ровно 100 вхождений AB
    (?:(?!AB).)*        # Любые символы после блока (без AB)
)
'''

matches = re.findall(pattern, content, flags=re.DOTALL | re.VERBOSE)
max_length = max(len(match) for match in matches) if matches else 0
print(max_length)