from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_geri():
    tim.backward(10)
def move_sag():
    tim.right(20)
def move_sol():
    tim.left(20)
def move_reset():
    tim.reset()




screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_geri)
screen.onkey(key="d", fun=move_sag)
screen.onkey(key="a", fun=move_sol)
screen.onkey(key="c", fun=move_reset)
screen.exitonclick()
