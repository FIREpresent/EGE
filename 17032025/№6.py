import turtle
t = turtle.Turtle()
turtle.tracer(0)
turtle.screensize(1000, 1000)
k = 30

for i in range(5):
    t.forward(9*k)
    t.right(90)
    t.forward(3*k)
    t.right(90)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()
