# import colorgram

# # Resimden renkleri çekme
# colors = colorgram.extract('resim.webp', 10)  # İlk 10 rengi çek



# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()


color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203)]



tim.right(135)
tim.forward(400)
tim.left(135)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.left(90)
    tim.forward(40)
    tim.left(90)
    tim.forward(500)
    tim.right(180)











screen = turtle_module.Screen()
screen.exitonclick()


