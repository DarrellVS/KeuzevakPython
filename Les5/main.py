from __car import *
from turtle import Turtle, Screen
import time 

# Create two cars
car1 = Car('brand1', 2, 20, 'red')
car2 = Car('brand2', 3, 25, 'blue')
TURTLE_SIZE = 20

# Create a screen and initialize it
screen = Screen()
screen.setup(600, 600)

# Create a turtle and initialize it
tr = Turtle(shape="classic", visible=True)

# Set its speed to 10
tr.speed(10)

# Rectangle drawing function
def drawRectangle(pos, width, height, fillColor):
    # Transform position to top left of window_width
    x = pos[0] + TURTLE_SIZE/2 - screen.window_width()/2
    y = screen.window_height()/2 - TURTLE_SIZE/2 - pos[1]

    # Translate
    tr.penup()
    tr.goto(x, y)
    tr.pendown()

    # Set color and begin filling
    tr.color(fillColor, fillColor)
    tr.begin_fill()

    # Draw rectangle
    for i in range(4):
        if(i % 2 == 0): tr.forward(width)   # If index is even, draw the width
        else: tr.forward(height)            # If index is uneven, draw the length
        tr.right(90)                        # Turn 90 degrees to the right

    # Stop filling
    tr.end_fill()

# State the previous time as the current time, to be updated in simulation loop
prevTime = time.time()

# Simulation loop, repeat indefinitely
while True:
    # Calculate the difference in time between the last draw and the current draw
    deltaTime = time.time() - prevTime

    # Print the car state
    car1.print()
    car2.print()

    # Simulate driving by translating according to the elapsed time
    car1.drive(deltaTime)
    car2.drive(deltaTime)

    # Clear the screen
    screen.clear()

    # Save the time a prev time to time the draw functions
    prevTime = time.time()

    # Draw the cars
    drawRectangle((175, round(car1.getPosition())), 50, 90, car1.getColor())
    drawRectangle((325, round(car2.getPosition())), 50, 90, car2.getColor())