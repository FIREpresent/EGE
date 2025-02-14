f = open('26_1.txt')
n = int(f.readline())
a = []
for i in f:
    prixod, dlitel, N_okna = [int(x) for x in i.split()]
    a.append([prixod, dlitel, N_okna])
a.sort()
okno_1 = []
okno_2 = []
count = 0
usli = 0
for prixod, dlitel, N_okna in a:
    while len(okno_1) > 0 and okno_1[0] <= prixod:
        del okno_1[0]
    while len(okno_2) > 0 and okno_2[0] <= prixod:
        del okno_2[0]
    if N_okna == 1 or (N_okna != 1 and N_okna != 2 and len(okno_1) <= len(okno_2)):
        if okno_1 == []:
            okno_1.append(prixod + dlitel)
            count += 1
        elif len(okno_1) < 14:
            okno_1.append(okno_1[-1] + dlitel)
            count +=1
        else:
            usli += 1
    else:
        if okno_2 == []:
            okno_2.append(prixod + dlitel)
        elif len(okno_2) < 14:
            okno_2.append(okno_2[-1] + dlitel)
        else:
            usli += 1
print(count, usli)