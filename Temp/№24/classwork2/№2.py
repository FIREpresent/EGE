with open('24-2.txt') as f:
    s = f.readline()
    s = s.replace('C', ' ').replace('F', ' ')
    vec = s.split(' ')
    print(len(max(vec, key=len)))
    print(vec)

