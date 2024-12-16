import turtle as t
k = 30

t.seth(90)
t.width(2)
t.speed(100)

for i in range(5):
    t.seth(0)
    t.circle(5*k,180)

    t.seth(90)
    t.circle(5*k,180)

    t.seth(180)
    t.circle(5*k,180)

    t.seth(270)
    t.circle(5*k,180)

t.up()
for x in range(-20, 20):
    for y in range(-20, 20):

        t.goto(x*k, y*k)
        t.dot(4)
t.up()
t.done()