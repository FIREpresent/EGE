import turtle
t = turtle.Turtle()
turtle.screensize(10000, 10000)
turtle.tracer(0)
k = 30

t.right(90)

for _ in range(2):
    t.forward(6*k)
    t.right(90)
    t.forward(12*k)
    t.right(90)

t.penup()

t.forward(k)
t.right(90)
t.forward(3*k)
t.left(90)

t.pendown()

for _ in range(2):
    t.forward(77 * k)
    t.right(90)
    t.forward(45 * k)
    t.right(90)

t.penup()
for x in range(-60, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()