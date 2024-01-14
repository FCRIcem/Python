from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")

# for _ in range(100):
#     tim.circle(100)
#     tim.forward(4)
#     tim.right(4)

def draw_spring(size_of):
    for _ in range(int(360 / size_of)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of)

draw_spring(5)



screen = Screen()
screen.exitonclick()
