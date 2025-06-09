with open('26-2-2.txt') as f:
    n, s = map(int, f.readline().split())
    l = list(map(int, f.readlines()))
l.sort(reverse=True)

# print(s)
# print(l[:100])
# print(l[-400:])

ships = []

while len(l) > 0:

    indxs_on_board = []
    local_ship = []

    for i in range(len(l)):
        if l[i] + sum(local_ship) <= s:
            indxs_on_board.append(i)
            local_ship.append(l[i])

    ships.append(local_ship)
    l = [l[i] for i in range(len(l)) if i not in indxs_on_board]

print(len(ships), sum(ships[-1]))