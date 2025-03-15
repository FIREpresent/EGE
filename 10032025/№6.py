import turtle
t = turtle.Turtle()
turtle.tracer(0)
turtle.screensize(1000, 1000)
k = 30

for i in range(9):
    t.forward(22*k)
    t.right(90)
    t.forward(6*k)
    t.right(90)

t.penup()
t.forward(1*k)
t.right(90)
t.forward(5*k)
t.left(90)
t.pendown()

for i in range(9):
    t.forward(53*k)
    t.right(90)
    t.forward(75*k)
    t.right(90)
t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()
