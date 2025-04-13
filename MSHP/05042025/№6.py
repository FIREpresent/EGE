import turtle
t = turtle.Turtle()
turtle.screensize(4000, 4000)
turtle.tracer(0)
k = 30
t.left(60)
for i in range(8):
    t.forward(6*k)
    t.left(60)
    t.forward(6*k)
    t.left(120)

t.penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.update()
turtle.mainloop()
turtle.done()
