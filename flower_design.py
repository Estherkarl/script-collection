import turtle
import math

# Function to draw a petal
def draw_petal(t, radius):
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)

# Function to draw a flower
def draw_flower(t, petal_radius, petal_count):
    angle = 360 / petal_count
    for _ in range(petal_count):
        draw_petal(t, petal_radius)
        t.right(angle)

# Initialize Turtle
screen = turtle.Screen()
screen.bgcolor("white")

flower_turtle = turtle.Turtle()
flower_turtle.shape("turtle")
flower_turtle.color("red")
flower_turtle.speed(10)

# Move turtle to starting position
flower_turtle.penup()
flower_turtle.goto(0, -200)
flower_turtle.pendown()

# Draw flower
petal_radius = 100
petal_count = 6
draw_flower(flower_turtle, petal_radius, petal_count)

# Hide turtle and display result
flower_turtle.hideturtle()
turtle.done()
d