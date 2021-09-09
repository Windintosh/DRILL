import turtle

b=0
n=0
while(n<5):
    turtle.forward(500)
    if(b==0):
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        b=1
    else:
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        b=0
    n = n+1

n=0
turtle.forward(500)
turtle.left(90)

while(n<5):
    turtle.forward(500)
    if(b==0):
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        b=1
    else:
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        b=0
    n = n+1

turtle.forward(500)
