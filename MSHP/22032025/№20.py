import turtle
t = turtle.Turtle()
turtle.screensize(2000, 2000)
turtle.tracer(0)
k = 30

for i in range(2):
    t.forward(13*k)
    t.right(90)
    t.forward(20*k)
    t.right(90)

t.penup()

t.forward(8*k)
t.right(90)
t.backward(3*k)
t.left(90)

t.pendown()

for i in range(2):
    t.forward(16*k)
    t.right(90)
    t.forward(8*k)
    t.right(90)

t.penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        t.setpos(x*k, y*k)
        t.dot()

turtle.update()
turtle.mainloop()
turtle.done()