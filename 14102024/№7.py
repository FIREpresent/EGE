import turtle as t
k = 20
t.speed(100)
for i in range(4):
    t.forward(k*8)
    t.right(90)

for j in range(3):
    t.forward(k*12)
    t.right(120)

t.up()
t.speed(100)

for x in range(15, -20, - 1):
    for y in range(5, -20, - 1):
        t.goto(x * k, y * k)
        t.dot(4)
#13 - ответ
t.done()