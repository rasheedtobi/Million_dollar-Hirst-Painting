import colorgram
import turtle
import random


te = turtle.Turtle()
turtle.colormode(255)
te.penup()
te.hideturtle()
te.speed('fastest')


def extract_colors(filename, num):
    colors = colorgram.extract(filename, num)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        n_color = (r, g, b)
        rgb_colors.append(n_color)
    # print(rgb_colors)
    return rgb_colors


def make_painting(num_dots):
    te.setheading(230)
    te.forward(300)
    te.setheading(0)

    spots_num = num_dots
    for dot in range(1, spots_num+1):
        color_list = extract_colors('hirst.jpg', 36)
        te.dot(20, random.choice(color_list))
        te.forward(50)

        if dot % 10 == 0:
            te.setheading(90)
            te.forward(50)
            te.setheading(180)
            te.forward(500)
            te.setheading(0)


# make_painting(150)
screen = turtle.Screen()
screen.exitonclick()
