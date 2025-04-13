with open('24-2.txt', 'r') as file:
    s = file.read().strip()

if not s:
    print("")
    print(0)
else:
    max_sequence = [s[0]]
    current_sequence = [s[0]]

    for i in range(1, len(s)):
        if ord(s[i]) < ord(current_sequence[-1]):
            current_sequence.append(s[i])
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence.copy()
            current_sequence = [s[i]]

    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence

    result_str = ''.join(max_sequence)
    print(result_str)
    print(len(result_str))