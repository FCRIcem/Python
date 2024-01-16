from turtle import Turtle, Screen
import random

def random_speed():
    return random.randint(-7, 10)

tim = Turtle()
tommy = Turtle()
emre = Turtle()
görkem = Turtle()

tim.penup()
tommy.penup()
emre.penup()
görkem.penup()

tim.shape('turtle')
tim.color('red')
tommy.shape('turtle')
tommy.color('blue')
emre.shape('turtle')
emre.color('purple')
görkem.shape('turtle')
görkem.color('green')

tim.goto(-300, 0)
tommy.goto(-300, -40)
emre.goto(-300, -80)
görkem.goto(-300, 40)

screen = Screen()

finish_line = 300

user_guess = screen.textinput("Kaplumbağa Yarışı", "Hangi kaplumbağa kazanacak? (Tim(red), Tommy(mavi), Emre(mor), Görkem(yeşil))")

while True:
    tim.forward(random_speed())
    tommy.forward(random_speed())
    emre.forward(random_speed())
    görkem.forward(random_speed())

    if tim.xcor() > finish_line:
        winner = "Tim"
        break
    elif tommy.xcor() > finish_line:
        winner = "Tommy"
        break
    elif emre.xcor() > finish_line:
        winner = "Emre"
        break
    elif görkem.xcor() > finish_line:
        winner = "Görkem"
        break

winner_turtle = Turtle()
winner_turtle.penup()
winner_turtle.hideturtle()
winner_turtle.goto(0, 0)
winner_turtle.color('black')
winner_turtle.write(f"Yarışı kazanan kaplumbağa: {winner}", align="center", font=("Arial", 16, "normal"))

if user_guess.lower() == winner.lower():
    print("Tebrikler! Doğru tahmin!")
else:
    print(f"Üzgünüm, doğru tahmin edemediniz. Kazanan kaplumbağa: {winner}")

screen.exitonclick()
