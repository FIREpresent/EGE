import turtle

t = turtle.Turtle()
turtle.screensize(2000, 2000)
turtle.tracer(0)
k = 30

for _ in range(5):
    t.forward(8*k)
    t.right(120)

    for _ in range(2):
        t.forward(4 * k)
        t.right(60)

    t.forward(4*k)
    t.right(120)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.mainloop()
turtle.done()