f = open('24.txt')
c = 0
s = f.readline()
s = s.split('A')
for i in range(1, len(s)):
    if s[i].count('B') == 0 and len(s[i]) + 2 >= 10:
        c += 1
print(c)
