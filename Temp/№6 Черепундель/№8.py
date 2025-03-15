import turtle
t = turtle.Turtle()
turtle.tracer(0)
turtle.screensize(3000, 3000)
k = 45

for i in range(4):
    t.forward(28*k)
    t.right(90)
    t.forward(26*k)
    t.right(90)

t.penup()
t.forward(8*k)
t.right(90)
t.forward(7*k)
t.left(90)
t.pendown()

for i in range(4):
    t.forward(67*k)
    t.right(90)
    t.forward(98*k)
    t.right(90)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()
