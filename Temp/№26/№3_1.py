f = open('26-3 (4).txt')
dur, n = map(int, f.readline().split())

plains = [list(map(int, i.split())) for i in f]

# Сортируем по времени окончания, так как
# чем раньше один кончится, тем раньше сможет начаться следующий
plains.sort(key=lambda x: (x[1], -x[0]))


# Уберем все рейсы, кончающиеся после закрытия аэропорта
ind = len(plains)
for i in range(len(plains)):
    if plains[i][1] > dur:
        ind = i
        break

plains = plains[:ind]

# Время окончания последнего рейса
last_end = plains[0][1]
cnt = 1
sm = plains[0][1] - plains[0][0]

for start, end in plains:
    # Может начаться новое - начинаем, не может - добавляем в список возможных
    if start >= last_end:
        cnt += 1
        last_end = end
        # Увеличиваем время общей длительности
        sm += end - start

print(cnt, sm)