import turtle
t = turtle.Turtle()
turtle.tracer(0)
turtle.screensize(1000, 1000)
k = 30

for i in range(15):
    t.forward(15*k)
    t.right(120)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()
