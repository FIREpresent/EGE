v = [int(elem) for elem in open('17_22469.txt')]
summ_nechet = 0
counter = 0
max_p = -10**100

for elem in v:
    if len(str(abs(elem))) == 5 and abs(elem) % 2 != 0:
        summ_nechet += elem

for i in range(len(v)-1):
    a = v[i]
    b = v[i+1]
    if ((abs(a) % 10 == abs(summ_nechet) % 10 and abs(b) % 10 != abs(summ_nechet) % 10)
            or (abs(b) % 10 == abs(summ_nechet) % 10 and abs(a) % 10 != abs(summ_nechet) % 10)):
        counter += 1
        max_p = max(max_p, a*b)

print(counter, max_p)

