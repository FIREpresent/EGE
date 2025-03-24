alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
with open('24-3.txt') as f:
    s = f.readline()
    for a in alph:
        s = s.replace(a, ' ')
    vec = s.split(' ')
    vec = vec[:-1]
    vec_1 = [int(elem) for elem in vec if len(elem) > 0 and int(elem) % 2 != 0]
    print(max(vec_1))

