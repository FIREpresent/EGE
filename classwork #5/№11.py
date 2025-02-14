f = open('26_1.txt')
n = int(f.readline())

confs = [list(map(int, i.split())) for i in f]

confs.sort(key=lambda x: (x[1], x[0]))

last_end = confs[0][1]
program = [confs[0]]
cnt = 1

for conf in confs:
    start, end = conf
    if start >= last_end:
        cnt += 1
        last_end = end
        program.append(conf)

new_end = program[-3][1]
maximum = 10 ** 10
for conf in range(confs.index(program[-3]) + 1, len(confs)):
    start, end = confs[conf]
    if start >= new_end:
        variants = [i[0] for i in confs[conf + 1:] if i[0] >= end]
        if variants:
            maximum = max(maximum, abs(max(variants) - end))

print(cnt, maximum)