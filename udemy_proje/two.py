from turtle import Turtle, Screen

cem = Turtle()

for _ in range(5):
    for _ in range(10):
        cem.forward(5)
        cem.penup()
        cem.forward(5)
        cem.pendown()



screen = Screen()
screen.exitonclick()