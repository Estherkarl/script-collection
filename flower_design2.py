from turtle import *
import colorsys

speed(0)
bgcolor("black")

h = 0
for i in range(16):
    pencolor(colorsys.hsv_to_rgb(h, 1, 1))
    for j in range(18):
        circle(150 - j * 6)
        rt(90)
    h += 0.005