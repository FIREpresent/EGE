import turtle
t = turtle.Turtle()
turtle.screensize(2000, 2000)
turtle.tracer(0)
k = 30

for i in range(2):
    t.forward(10*k)
    t.right(90)
    t.forward(20*k)
    t.right(90)

t.penup()

t.forward(5*k)
t.right(90)
t.forward(7*k)
t.left(90)

t.pendown()

for i in range(2):
    t.forward(20*k)
    t.right(90)
    t.forward(40*k)
    t.right(90)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.update()
turtle.mainloop()
turtle.done()