import turtle
t = turtle.Turtle()
turtle.screensize(1000, 1000)
turtle.tracer(0)
k = 30

t.right(30)
for i in range(6):
    t.forward(7*k)
    t.right(120)
    t.forward(7*k)
    t.right(60)

t.penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.update()
turtle.mainloop()
turtle.done()
