from turtle import *
import colorsys

speed(0)
bgcolor("black")

# Define colors in HSV format
colors = [(0.5, 1, 1),  # pink
          (0.3, 1, 1),  # yellow
          (0.7, 1, 1),  # light blue
          (0.9, 1, 1)]  # purple

h = 0
for i in range(36):
    pencolor(colorsys.hsv_to_rgb(colors[i % len(colors)][0], colors[i % len(colors)][1], colors[i % len(colors)][2]))
    width(i / 100 + 1)
    for j in range(6):
        fd(100)
        rt(60)
    h += 10
