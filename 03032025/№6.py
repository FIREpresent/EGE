import turtle
t = turtle.Turtle()
turtle.screensize(10000, 10000)
turtle.tracer(0)
t.reset()

t.seth(90)
t.width(2)
t.speed(20)

k = 30

t.right(180)
t.forward(5*k)
t.right(90)
t.forward(50*k)
t.right(90)
t.forward(5*k)

for i in range(5):
    t.seth(90)
    t.circle(-5 * k, 180)
t.penup()

for x in range(-60, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()







