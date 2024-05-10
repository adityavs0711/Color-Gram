import random
import turtle as t
import colorgram

colors_list = []
colors = colorgram.extract("image.jpeg", 30)
for item in colors:
    color = (item.rgb.r, item.rgb.g, item.rgb.b)
    colors_list.append(color)

t.colormode(255)

timmy = t.Turtle()
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()
x_cor = -250
y_cor = -250


def dot_and_move():
    chosen_color = random.choice(colors_list)
    timmy.dot(20, chosen_color)
    timmy.forward(50)


def draw_row(row_number):
    timmy.setx(x_cor)
    timmy.sety(y_cor + 50 * row_number)
    for _ in range(10):
        dot_and_move()


for i in range(1, 11):
    draw_row(i)


screen = t.Screen()
screen.exitonclick()
