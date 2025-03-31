with open('24-2.txt') as f:
    s = f.readline()
    s = s.replace('A', ' ').replace('E', ' ')
    arr = s.split(' ')
    print(len(max(arr, key=len)))
