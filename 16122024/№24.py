f = open('24.txt')
s = f.readline()
s = s.replace('-', '*').replace('B', ' ').replace('C', ' ').replace('D', ' ').replace('2', '1').replace('3', '1').replace('4', '1').replace('5', '1').replace('6', '1')
s = s.replace('1A', '1 A').replace('**', '* *').replace('AA', 'A A').replace('*A', '* A').replace('A*', 'A *')
s = sorted(s.split(), key=len, reverse=1)

v = []
for string in s:
    if string[-1] == '*':
        string = string[:-1]
    if len(string) > 0:
        if string[0] == 'A' and string.count('A') == 1:
            v.append(len(string))
f.close()
print(max(v))