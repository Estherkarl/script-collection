import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle for drawing
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)
spiral_turtle.width(2)

# Number of circles in the spiral
num_circles = 100

# Draw the spiral pattern
for i in range(num_circles):
    # Calculate color using HSV color space
    hue = float(i) / num_circles
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

    # Set pen color
    spiral_turtle.color(color)

    # Draw a circle
    spiral_turtle.circle(i * 3)

    # Move the turtle to the left
    spiral_turtle.left(59)

# Hide the turtle and display the result
spiral_turtle.hideturtle()
turtle.done()
