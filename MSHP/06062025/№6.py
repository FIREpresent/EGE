import turtle
t = turtle.Turtle()
turtle.screensize(10000, 10000)
turtle.tracer(0)
k = 30

for _ in range(2):
    t.forward(24*k)
    t.right(90)
    t.forward(10*k)
    t.right(90)

t.forward(3*k)
t.left(90)
t.forward(13*k)
t.right(90)

for _ in range(2):
    t.forward(9 * k)
    t.right(90)
    t.forward(32 * k)
    t.right(90)

t.penup()

for x in range(-60, 60):
    for y in range(-60, 60):
        t.setpos(x*k, y*k)
        t.dot()

turtle.mainloop()
turtle.done()
