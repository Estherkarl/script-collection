from turtle import *
import colorsys

# Set up the screen
bgcolor('black')
tracer(200)
width(6)

# Set initial parameters
length = 500
h = 0

# Move turtle to the center of the screen
up()
goto(0, 0)
down()

# Adjust the starting position based on the length to keep the spiral centered
x_start = -length / 2
y_start = -length / 2
up()
goto(x_start, y_start)
down()

# Draw the spiral pattern
while length > 1:
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005
    circle(length, 120)
    left(75)
    length -= 1

# Finish drawing
done()
