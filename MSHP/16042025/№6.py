import turtle
t = turtle.Turtle()
turtle.screensize(10000, 10000)
turtle.tracer(0)
k = 30

for _ in range(2):
    t.forward(7*k)
    t.right(90)
    t.forward(4*k)
    t.right(90)

t.penup()

t.forward(2*k)
t.right(90)
t.forward(5*k)
t.left(90)

t.pendown()

for _ in range(2):
    t.forward(3*k)
    t.right(90)
    t.forward(4*k)
    t.right(90)

t.penup()
for x in range(-60, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()







