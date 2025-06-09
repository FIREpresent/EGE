import turtle
t = turtle.Turtle()
turtle.screensize(10000, 10000)
turtle.tracer(0)
k = 30

t.right(90)

for _ in range(3):
    t.right(45)
    t.forward(10*k)
    t.right(45)

# t.penup()

t.right(315)
t.forward(10*k)

# t.pendown()

for _ in range(2):
    t.right(90)
    t.forward(10*k)

t.penup()
for x in range(-60, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()







