import turtle
t = turtle.Turtle()
turtle.screensize(1000, 1000)
turtle.tracer(0)
k = 30

for i in range(2):
    t.forward(10*k)
    t.right(90)
    t.forward(20*k)
    t.right(90)

t.penup()

t.backward(15*k)
t.right(90)
t.backward(10*k)
t.left(90)

t.pendown()

for i in range(2):
    t.forward(20*k)
    t.right(90)
    t.forward(25*k)
    t.right(90)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.update()
turtle.mainloop()
turtle.done()