import turtle

t = turtle.Turtle()
turtle.screensize(10000, 10000)
turtle.tracer(0)
k = 20

t.pendown()

for _ in range(4):
    t.forward(50*k)
    t.left(90)

t.penup()
t.forward(50*k)
t.left(135)
t.pendown()

for _ in range(2):
    t.forward(102*k)
    t.left(120)
    t.forward(182*k)
    t.left(60)

t.penup()

for x in range(-100, 100):
    for y in range(-100, 100):
        t.setpos(x*k, y*k)
        t.dot()

turtle.mainloop()
turtle.done()
