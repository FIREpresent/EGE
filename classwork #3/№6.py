from turtle import *
size = 50
screensize(2000,2000)
tracer(0)
down()

for i in range(6):
    forward(13*size)
    right(120)
up()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x * size,y * size)
        dot(4,'blue')
done()

#33*2