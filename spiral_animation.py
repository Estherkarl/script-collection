from turtle import *
import colorsys

bgcolor('black')
tracer(200)
width(6)
length = 500
h = 0

up()
goto(-300, 0)
down()

while length > 1:
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005
    circle(length, 120)
    lt(75)
    length -= 1

done()
