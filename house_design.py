import turtle

# Function to draw a rectangle
def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a triangle
def draw_triangle(t, width, height, color):
    t.begin_fill()
    t.color(color)
    for _ in range(3):
        t.forward(width)
        t.left(120)
    t.end_fill()

# Function to draw a parallelogram
def draw_parallelogram(t, width, height, angle, color):
    t.begin_fill()
    t.color(color)
    t.left(angle)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120 - angle)
    t.end_fill()

# Function to draw a circle
def draw_circle(t, radius, color):
    t.begin_fill()
    t.color(color)
    t.circle(radius)
    t.end_fill()

# Function to draw a big house
def draw_big_house():
    # Initialize Turtle
    house_turtle = turtle.Turtle()
    house_turtle.speed(5)

    # Draw main building
    draw_rectangle(house_turtle, 300, 200, "lightblue")

    # Draw roof
    draw_triangle(house_turtle, 340, 100, "brown")

    # Draw door
    draw_rectangle(house_turtle, 60, 100, "gray")

    # Draw windows
    house_turtle.penup()
    house_turtle.goto(-120, 20)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 50, 50, "yellow")

    house_turtle.penup()
    house_turtle.goto(70, 20)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 50, 50, "yellow")

    # Draw chimney
    house_turtle.penup()
    house_turtle.goto(120, 100)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 20, 80, "gray")

    house_turtle.penup()
    house_turtle.goto(130, 180)
    house_turtle.pendown()
    draw_triangle(house_turtle, 40, 20, "gray")

    # Draw garage
    house_turtle.penup()
    house_turtle.goto(-220, -100)
    house_turtle.pendown()
    draw_parallelogram(house_turtle, 120, 80, 30, "lightblue")

    # Draw garage door
    draw_rectangle(house_turtle, 100, 60, "gray")

    # Draw driveway
    house_turtle.penup()
    house_turtle.goto(-300, -100)
    house_turtle.pendown()
    house_turtle.goto(-220, -100)

    # Draw garden
    house_turtle.penup()
    house_turtle.goto(-300, -200)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 300, 100, "green")

    # Draw sun
    house_turtle.penup()
    house_turtle.goto(200, 250)
    house_turtle.pendown()
    draw_circle(house_turtle, 30, "yellow")

    # Hide turtle after drawing
    house_turtle.hideturtle()

    # Keep window open until manually closed
    turtle.done()

# Call the function to draw the big house
draw_big_house()
