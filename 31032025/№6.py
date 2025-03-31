import turtle
t = turtle.Turtle()
turtle.screensize(4000, 4000)
turtle.tracer(0)
k = 30
t.right(90)
for i in range(4):
    t.forward(4*5**0.5*k)
    t.right(150)
    t.forward(4*5**0.5*k)
    t.right(300)

t.penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.update()
turtle.mainloop()
turtle.done()
