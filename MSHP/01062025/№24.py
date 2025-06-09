# f = open('24.txt')
# s = f.readline()
# s = s.replace('DE', 'X')

s = 'ABCDEABDDEABCCBADEABOBABEBRADE'
s = s.replace('DE', 'X')
v = []
summ = ''
k_x = 0
for elem in s:
    if elem == 'X':
        if k_x < 2:
            k_x += 1
            summ += elem
        else:
            v.append([summ, len(summ)])
            print()
            k_x = 0
    if elem != 'X':
        summ += elem

print(v)