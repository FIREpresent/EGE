
f = open('27-B.txt')
s = f.readlines()
count = 0

for i in range(1, len(s)):
    for j in range(i+1, len(s)):
        if str(int(s[i]) * int(s[j]))[-7:] == '0000000' and str(int(s[i]) * int(s[j]))[-8:] != '00000000':
            count += 1
print(count)