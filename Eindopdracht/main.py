from math import log
import pyglet, sys
from pyglet import shapes

from __map import *
from __ship import *
from __socket import *



# Construct a sizes dictionary 
sizes = {
    'mapGrid': {
        'width': 20,
        'height': 10
    },

    'window': {
        'width': 1000,
        'height': 500
    }
}
sizes['gridEntry'] = {
    'width': sizes['window']['width'] / sizes['mapGrid']['width'],
    'height': sizes['window']['height'] / sizes['mapGrid']['height']
}

# Construct a grid lines dictionary
lines = {
    'horizontal': [None for i in range(sizes['mapGrid']['width'] - 1)],
    'vertical': [None for i in range(sizes['mapGrid']['height'] - 1)]
}




# Initialize a Map, socket
myMap = Map(sizes)
opponentMap = None
socket = Socket('https://python.darrellvs.nl')

# Connect the websocket to the server
# socket.connect()

# Create a pyglet window, eventloop and graphics batch
window = pyglet.window.Window(1000, 500)
eventLoop = pyglet.app.EventLoop()
batch = pyglet.graphics.Batch()


# State of ship placement
amountOfShips = 0;


# Window event handlers
@window.event
def on_draw():
    window.clear()
    drawMap()

@window.event
def on_mouse_motion(x, y, dx, dy):
    return

@window.event
def on_mouse_press(x, y, button, modifiers):
    global amountOfShips
    index = myMap.getCorrespondingMatrixIndex(x, y);

    if(amountOfShips == 8):
        if(opponentMap is None):
            print("Your opponent has not yet finished placing all of their ships, please wait.")

        else:
            print(opponentMap.getEntry(index[0], index[1]))

    else:
        couldPlace = myMap.placeShip(MediumShip('south'), index[0], index[1])

        if(couldPlace): 
            amountOfShips += 1

            if(amountOfShips == 8):
                print('placing finished.')
                myMap.print();
                print(myMap.getShareableMatrix())

        else: 
            print("Could not place ship due to collision or map boudnaries.") 

@window.event
def on_close():
    window.close()
    socket.disconnect()
    print('Running services closed successfully, exiting...')



def drawMap():
    entryWidth = sizes['gridEntry']['width']
    entryHeight = sizes['gridEntry']['height']
    crosses = [ [ [0,0] for i in range(sizes['mapGrid']['width']) ] for j in range(sizes['mapGrid']['height']) ]

    # For each grid item width
    for i in range(sizes['mapGrid']['width'] - 1):
        x = round(i * entryWidth + entryWidth)
        lines['horizontal'][i] = shapes.Line(x, 0, x, sizes['window']['height'], 1, (150, 150, 150), batch = batch)

    # For each grid item height
    for i in range(sizes['mapGrid']['height'] - 1):
        y = round(i * entryHeight + entryHeight)
        lines['vertical'][i] = shapes.Line(0, y, sizes['window']['width'], y, 1, (150, 150, 150), batch = batch)

    # Get matrix from map object
    matrix = myMap.getMatrix()

    # loop over matrix and place ship crosses wherever needed
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            # If the current element in the matrix is a ship
            if(isinstance(matrix[i][j], Ship)):

                # Get the length of the ship
                length = matrix[i][j].getLength()

                # Construct the cross' x and y position (top left corner of grid entry)
                x2 = entryWidth * j
                y2 = entryHeight * (9 - i)

                # Construct a color based on the ship's length
                color = (0, 255, 0) if length == 1 else (0, 0, 255) if length == 2 else (255, 0, 0)

                # Draw crosses
                crosses[i][j][0] = shapes.Line(x2, y2, x2 + entryWidth, y2 + entryHeight, 1, color, batch = batch)
                crosses[i][j][1] = shapes.Line(x2 + entryWidth, y2, x2, y2 + entryHeight, 1, color, batch = batch)

    # Draw the batch
    batch.draw()


pyglet.app.run()