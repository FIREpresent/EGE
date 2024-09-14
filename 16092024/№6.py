import turtle as t
k = 70

t.speed(100)
for i in range(12):
    t.right(60)
    t.forward(1 * k)
    t.right(60)
    t.forward(1 * k)
    t.right(270)

t.up()
t.speed(100)

for x in range(5, -20, - 1):
    for y in range(5, -20, - 1):
        t.goto(x * k, y * k)
        t.dot(4)
#1 + 4 + 5 + 4 + 6 + 6*3 = 38 - ответ
t.done()
