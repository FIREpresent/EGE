from pygame.key import key_code

with open('24-1.txt') as f:
    s = 'QWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    s = sorted(s)
    v = dict()

    for a in s:
        v[a] = -10**10

    arr = f.readline()
    count = 0
    print(v)

    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            print(arr[i], arr[i+1])
            v[arr[i]] = max(count + 1, v[arr[i]])
            count = 0
        else:
            count += 1
    print(v)
    print(v, key = lambda x: v[x])

    #     dict[a] = max(dict[a], maximum)
    # arr = f.readline()

