#Hunter Standifer
#koch.py

import turtle

def drawFractalLine(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        drawFractalLine(t, length, level-1)
        t.left(60)
        drawFractalLine(t, length, level-1)
        t.right(120)
        drawFractalLine(t, length, level-1)
        t.left(60)
        drawFractalLine(t, length, level-1)

def drawKochSnowflake(t, length, level):
    for i in range(3):
        drawFractalLine(t, length, level)
        t.right(120)

t = turtle.Turtle()
level = int(input("Enter the fractal level: "))

# Draw the Koch snowflake
drawKochSnowflake(t, 400, 2)







