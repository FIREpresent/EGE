s = open("24.txt").read()
s = s.replace('CD', 'C D')

s = s.split()
maximum = -1
for i in range(len(s)):
    row = ''.join(s[i:i + 141])
    maximum = max(maximum, len(row))
print(maximum)