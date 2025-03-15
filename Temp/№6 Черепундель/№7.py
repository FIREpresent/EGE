import turtle
t = turtle.Turtle()
turtle.tracer(0)
turtle.screensize(3000, 3000)
k = 45

for i in range(3):
    t.forward(7*k)
    t.right(90)
    t.forward(12*k)
    t.right(90)

t.penup()
t.forward(4*k)
t.right(90)
t.forward(6*k)
t.left(90)
t.pendown()

for i in range(4):
    t.forward(83*k)
    t.right(90)
    t.forward(77*k)
    t.right(90)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()
