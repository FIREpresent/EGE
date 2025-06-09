with open('26-2-2.txt') as f:
    n, s = map(int, f.readline().split())
    l = list(map(int, f.readlines()))
l.sort(reverse=True)

# print(s)
# print(l[:100])
# print(l[-400:])

ships = []

while len(set(l)) > 1:

    local_ship = []

    for i in range(len(l)):
        if l[i] + sum(local_ship) <= s and l[i] != 0:
            local_ship.append(l[i])
            l[i] = 0

    ships.append(local_ship)

print(len(ships), sum(ships[-1]))