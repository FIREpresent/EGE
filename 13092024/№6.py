import turtle as t
k = 30

t.speed(100)
t.right(45)
for i in range(7):
    t.forward(k*5)
    t.right(45)
    t.forward(10 * k)
    t.right(135)

t.up()
t.speed(100)

for x in range(5, -20, - 1):
    for y in range(5, -20, - 1):
        t.goto(x * k, y * k)
        t.dot(5)
#9 + 9 + 9 = 27 - ответ
t.done()