import turtle as t
t.screensize(2000,2000)
k = 30
t.right(90)
t.forward(30)
t.right(90)
t.speed(1000)
for i in range(6):
    t.forward(10*k)
    t.right(60)

t.up()
t.speed(10000)
for x in range(-16, 60):
    for y in range(-10, 20):
        t.setpos(x * k, y * k)
        t.dot(4, 'red')

t.done()
#ответ: 268

