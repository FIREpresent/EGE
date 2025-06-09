import turtle
t = turtle.Turtle()
turtle.screensize(2000, 2000)
turtle.tracer(0)
k = 100
t.right(30)
for _ in range(3):
    t.right(150)
    t.forward(6*k)
    t.right(30)
    t.forward(12*k)
t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()

turtle.mainloop()
turtle.done()
