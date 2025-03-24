import turtle
t = turtle.Turtle()
turtle.screensize(2000, 2000)
turtle.tracer(0)
k = 15

t.right(180)
t.forward(2*k)
t.right(90)
t.forward(40*k)
t.right(90)
t.forward(2*k)
for _ in range(4):
    t.seth(0)
    t.circle(-5 * k, 180)

t.penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.setpos(x*k, y*k)
        t.dot(size=2)

turtle.update()
turtle.mainloop()
turtle.done()