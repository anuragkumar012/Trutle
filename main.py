
from turtle import *
from colorsys import *

speed(0)
bgcolor("black")
h = 0

for i in range(75):
    color = hsv_to_rgb(h, 1, 1)  # Returns RGB values between 0–1
    pencolor(color)
    h += 0.014
    left(1)
    forward(1)
    for _ in range(3):
        left(2)
        circle(150)

hideturtle()
done()

