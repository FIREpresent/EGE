f = open("24.txt")
s = f.readline()
a = [0] * 26
maxi = 0
for i in range(len(s) - 1):
    if s[i] == 'E':
        a[ord(s[i + 1]) - 65] += 1
for i in range(26):
    if a[i] > maxi:
        maxi = a[i]
        index = i
print(chr(index + 65))