import turtle
t = turtle.Turtle()
turtle.screensize(2000, 2000)
turtle.tracer(0)
k = 30
for _ in range(10):
    t.setpos(2*k, 15*k)


t.penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.mainloop()
turtle.done()