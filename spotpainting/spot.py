# import colorgram
# from colorgram import Color
# rgb_color=[]
# colors =  colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#
#     rgb_color.append((r,g,b))
# print(rgb_color)
import random
from turtle import Turtle, Screen,colormode
colormode(255)
color_list = [(173, 71, 45), (27, 33, 65), (243, 233, 71), (56, 87, 147), (220, 139, 92), (51, 38, 30), (132, 32, 47), (126, 160, 208), (224, 80, 52), (210, 82, 124), (41, 49, 128), (139, 33, 26), (148, 55, 76), (63, 30, 39), (88, 111, 206), (125, 183, 133), (33, 48, 39), (197, 135, 158), (73, 76, 40), (70, 106, 56), (164, 187, 238), (154, 138, 68), (41, 76, 59), (241, 161, 152), (227, 171, 187), (156, 202, 220)]


tim =  Turtle()
tim.teleport()
for i in range(0,500,50):
    for j in range(0,500,50):
        tim.teleport(j,i)
        tim.penup()
        tim.dot(20,random.choice(color_list))

tim.hideturtle()
Screen().exitonclick()

