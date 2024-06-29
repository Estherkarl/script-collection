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
    draw_rectangle(house_turtle, 300, 200, "#f4a261")  # Main building in a light brown color

    # Draw roof
    draw_triangle(house_turtle, 340, 100, "#2a9d8f")  # Roof in a teal color

    # Draw windows
    house_turtle.penup()
    house_turtle.goto(-100, 50)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 80, 80, "#264653")  # Window 1
    house_turtle.penup()
    house_turtle.goto(120, 50)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 80, 80, "#264653")  # Window 2

    # Draw door
    house_turtle.penup()
    house_turtle.goto(10, -100)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 80, 120, "#e76f51")  # Door in a salmon color
    house_turtle.penup()
    house_turtle.goto(40, -100)
    house_turtle.pendown()
    draw_circle(house_turtle, 10, "#f4a261")  # Door knob in a light brown color

    # Draw chimney
    house_turtle.penup()
    house_turtle.goto(-150, 100)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 20, 80, "#264653")  # Chimney base
    house_turtle.penup()
    house_turtle.goto(-150, 180)
    house_turtle.pendown()
    draw_triangle(house_turtle, 40, 20, "#264653")  # Chimney top

    # Draw windows on the roof
    house_turtle.penup()
    house_turtle.goto(-60, 150)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 60, 50, "#e9c46a")  # Window 1 on the roof
    house_turtle.penup()
    house_turtle.goto(0, 150)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 60, 50, "#e9c46a")  # Window 2 on the roof
    house_turtle.penup()
    house_turtle.goto(60, 150)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 60, 50, "#e9c46a")  # Window 3 on the roof

    # Draw landscaping - grass
    house_turtle.penup()
    house_turtle.goto(-400, -200)
    house_turtle.pendown()
    draw_rectangle(house_turtle, 800, 200, "#2a9d8f")  # Grass in a teal color

    # Draw sun
    house_turtle.penup()
    house_turtle.goto(300, 250)
    house_turtle.pendown()
    draw_circle(house_turtle, 40, "#e9c46a")  # Sun in a light yellow color

    # Hide turtle after drawing
    house_turtle.hideturtle()

    # Keep window open until manually closed
    turtle.done()

# Call the function to draw the big house
draw_big_house()
