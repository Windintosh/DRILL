import turtle

def go_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def go_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def go_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()


def go_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(go_up, 'w')
turtle.onkey(go_down, 's')
turtle.onkey(go_left, 'a')
turtle.onkey(go_right, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()

