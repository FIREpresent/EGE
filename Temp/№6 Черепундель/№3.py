import turtle
t = turtle.Turtle()
turtle.screensize(1000, 1000)
turtle.tracer(0)
k = 30

for i in range(2):
    t.forward(9*k)
    t.right(90)
    t.forward(15*k)
    t.right(90)

t.penup()

t.forward(12*k)
t.right(90)

t.pendown()

for i in range(2):
    t.forward(6*k)
    t.right(90)
    t.forward(12*k)
    t.right(90)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.update()
turtle.mainloop()
turtle.done()