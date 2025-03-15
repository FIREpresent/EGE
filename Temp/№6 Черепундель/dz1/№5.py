import turtle
t = turtle.Turtle()
turtle.tracer(0)
turtle.screensize(3000, 3000)
k = 45

#t.backward(100*k)
#t.forward(200*k)
#t.setposition(0, 0)

for i in range(2):
    t.left(120)

for i in range(10):
    t.right(30)
    t.forward(4*k)
    t.right(60)

t.penup()
t.left(150)
t.backward(2*k)
t.left(90)
t.backward(2*k)
t.pendown()

# for i in range(2):
#     t.forward(20*k)
#     t.right(90)
#     t.forward(25*k)
#     t.right(90)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
turtle.update()
turtle.mainloop()
turtle.done()
