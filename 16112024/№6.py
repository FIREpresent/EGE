import turtle as t
k = 20

t.speed(100)
for i in range(2):
    t.forward(k*24)
    t.right(90)
    t.forward(10 * k)
    t.right(90)

t.forward(3*k)
t.left(90)
t.forward(13*k)
t.right(90)

for i in range(2):
    t.forward(k*9)
    t.right(90)
    t.forward(32 * k)
    t.right(90)
t.up()
for x in range(25, -20, - 1):
    for y in range(30, -30, - 1):
        t.goto(x * k, y * k)
        t.dot(5)
#12 * 10 = 120 - ответ
t.done()