#Hunter Stanidfer
#Circle.py
import turtle
import math

def drawCircle(t, x, y, radius):
    # Move to the starting point of the circle
    t.penup()
    t.goto(x + radius, y)
    t.pendown()
    
    # Calculate the step distance
    step_distance = 2.0 * math.pi * radius / 120.0

    # Draw the circle
    for _ in range(120):
        t.forward(step_distance)
        t.left(3)

# Prompt the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Example usage
t = turtle.Turtle()
drawCircle(t, 0, 0, radius)
turtle.done()

