import turtle
t = turtle.Turtle()
turtle.screensize(4000, 4000)
turtle.tracer(0)
k = 30
t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10*k)
    t.right(45)

t.right(315)
t.forward(10*k)

for i in range(2):
    t.right(90)
    t.forward(10*k)

t.penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.update()
turtle.mainloop()
turtle.done()
