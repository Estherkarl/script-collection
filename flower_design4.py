import turtle
import math
import colorsys

# Function to draw a petal
def draw_petal(t, radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)
    t.end_fill()

# Function to draw a flower with petals of different colors
def draw_flower(t, petal_radius, petal_count, colors):
    angle = 360 / petal_count
    for i in range(petal_count):
        color = colors[i % len(colors)]
        draw_petal(t, petal_radius, color)
        t.right(angle)

# Initialize Turtle
screen = turtle.Screen()
screen.bgcolor("white")

flower_turtle = turtle.Turtle()
flower_turtle.shape("turtle")
flower_turtle.speed(5)

# Move turtle to starting position
flower_turtle.penup()
flower_turtle.goto(0, -200)
flower_turtle.pendown()

# Define colors for the petals of smaller flowers
petal_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the main flower with petals of different colors
petal_radius = 100
petal_count = 6
draw_flower(flower_turtle, petal_radius, petal_count, petal_colors)

# Hide turtle and display result
flower_turtle.hideturtle()
turtle.done()
