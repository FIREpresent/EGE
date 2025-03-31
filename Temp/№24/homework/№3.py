with open('24-3.txt') as f:
    alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    s = f.readline()
    for elem in alph:
        s = s.replace(elem, ' ')
    arr = s.split(' ')
    vec = [elem for elem in arr if len(elem) > 0][:-1]
    arr = list(map(int, vec))
    minimum = 10**10
    for elem in arr:
        if elem % 2 != 0:
            minimum = min(minimum, elem)
    print(minimum)
