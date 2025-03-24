with open('24-1.txt') as f:
    s = f.readline()
    s = s.replace('A', ' ').replace('B', ' ')
    vec = s.split(' ')
    print(len(max(vec, key=len)))

