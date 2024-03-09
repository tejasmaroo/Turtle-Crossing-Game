from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(0, -280)
turtle1.setheading(90)


def move():
    turtle1.forward(20)


def finish_line():
    if turtle1.ycor() > 280:
        return True


screen.listen()
screen.onkey(move, "space")

if finish_line():
    turtle1.goto(0, -280)
screen.exitonclick()
