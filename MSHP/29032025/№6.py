import turtle
t = turtle.Turtle()
turtle.tracer(0)
turtle.screensize(3000, 3000)
k = 45

for i in range(3):
    t.forward(4*k)
    t.left(270)
    t.forward(7*k)
    t.right(90)

t.left(315)

for i in range(4):
    t.forward(7*k)
    t.right(90)
    t.forward(4*k)
    t.left(270)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()
