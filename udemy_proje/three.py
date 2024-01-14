from turtle import Turtle, Screen
import random

cems = Turtle()

colours = ["red","blue","green","purple"]


def cizim_sekli(kenar_sayisi):
    angle = 360 / kenar_sayisi
    for _ in range (kenar_sayisi):
        cems.forward(100)
        cems.right(angle)

for _ in range (3, 11):
    cems.color(random.choice(colours))
    cizim_sekli(_)
    




screen = Screen()
screen.exitonclick()