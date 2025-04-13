s = open('24.txt').readline()
subs = ''
maxLen = 0
for char in s:
    if char.isdigit():
        if len(subs) > 0 and subs[-1] == '0' and (len(subs) == 1 or subs[-2] in '-*'):
            subs = char
        else:
            subs += char
        maxLen = max(len(subs), maxLen)
    elif char in '-*':
        if len(subs) > 0 and subs[-1] in '-*':
            subs = ''
        else:
            subs += char
print(maxLen)