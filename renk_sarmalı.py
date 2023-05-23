import turtle

colors = ["cyan","yellow","blue","green","white","red"]

p = turtle.Pen()
turtle.bgcolor("black")

for i in range(300):
    p.pencolor(colors[i%6])
    p.width(i/100+2)
    p.forward(i)
    p.left(59)