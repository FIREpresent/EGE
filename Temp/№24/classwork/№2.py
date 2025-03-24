max_ = 0
with open('17.txt') as f:
    s = f.readline()
    l = s.split('CD')
    b = 160

    for x in range(len(l) - b):
        count = 0
        if x != 0:
            count += 1
        if x != len(l)-b-1:
            count += 1
        str_ = 'CD'.join(l[x: x + b + 1])
        max_ = max(max_, len(str_)+count)

print(max_)