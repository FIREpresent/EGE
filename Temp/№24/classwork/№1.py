with open('24.txt') as f:
    s = f.readline()
    s = s.replace('C', ' ').replace('D', ' ')
    arr = s.split(' ')
    arr.sort(key=len)
    print(len(arr[-1]))
#replace, split

