from math import log
import pyglet, sys
from pyglet import shapes
from pyglet.window import key

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




# Initialize a Map
myMap = Map(sizes)

# Initialize a socket
socket = Socket('http://localhost:3012', myMap, sizes)

# Connect the websocket to the server
socket.connect()

# Create a pyglet window, eventloop and graphics batch
window = pyglet.window.Window(1000, 500)
eventLoop = pyglet.app.EventLoop()
batch = pyglet.graphics.Batch()

# State of ship placement
amountOfShips = 0
maxShips = 8

# 2 Small ships, 3 Medium and Large ships
ships = [None, [False, False], [False, False, False], [False, False, False]]
orientation = 'south'
shipLength = 1



# Window event handlers
@window.event
def on_draw():
    drawElements()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global amountOfShips, orientation, shipLength, winner
    index = myMap.getCorrespondingMatrixIndex(x, y)

    if(amountOfShips == maxShips):
        if(socket.getOpponentMap() is None):
            print("Your opponent has not yet finished placing all of their ships, please wait.")

        else:
            # The opponent has finished placing their ships
            # Validate if you have the semafore
            if(not socket.hasSemafore()):
                print('Its not your turn yet, please wait :)')
                return;

            # Get the opponent's map
            opponentMap = socket.getOpponentMap()
            clickedElement = opponentMap.getEntry(index[0], index[1])

            # If the clicked element is a ship instance
            if(isinstance(clickedElement, Ship)):

                # If the element is not yet destroyed
                if(clickedElement.isDestroyed() == False):
                    # Destroy the ship
                    opponentMap.destroyShip(clickedElement)
                    socket.destroyOpponentShip([index[0], index[1]])

                    # If player has won 
                    if(opponentMap.getAmountOfDestroyedShips() == maxShips):
                        socket.win() # Emit win event through socket


            # Pass the semafore to the opponent
            socket.sendSemafore();

    else:
        # Filter the ships placed list
        filteredList = list(filter(lambda item: item == False, ships[shipLength]))

        # If all ships for the selected length have been placed
        if(len(filteredList) == 0):
            return print("You have already placed the maximum amount of ships with length", shipLength)

        # Set next item in ships placed list for ship length to True
        ships[shipLength][len(ships[shipLength]) - len(filteredList)] = True

        # Place ship if it can
        couldPlace = myMap.placeShip(
            SmallShip(orientation) if shipLength == 1 else MediumShip(orientation) if shipLength == 2 else LargeShip(orientation)
        , index[0], index[1])

        # If it placed the ship
        if(couldPlace): 
            amountOfShips += 1

            # If the player has finished placing
            if(amountOfShips == maxShips):
                # Get the shareable map from the Map object and send it to the server
                print('placing finished.')
                shareableMatrix = myMap.getShareableMatrix()
                socket.finishedPlacement(shareableMatrix)

        # If it did not place the ship
        else: 
            print("Could not place ship due to collision or map boudnaries.") 

@window.event
def on_close():
    window.close()
    socket.disconnect()
    print('Running services closed successfully, exiting...')

@window.event
def on_key_press(symbol, modifiers):
    global orientation, shipLength
    if(symbol == key.DOWN): orientation = 'south'
    if(symbol == key.RIGHT): orientation = 'east'
    if(symbol == key._1): shipLength = 1
    if(symbol == key._2): shipLength = 2
    if(symbol == key._3): shipLength = 3



def drawElements(dt = None):
    window.clear()
    drawMap()
    drawLabels()

def drawMap():
    entryWidth = sizes['gridEntry']['width']
    entryHeight = sizes['gridEntry']['height']
    shapesList = []

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

                if(matrix[i][j].isDestroyed()):
                    # Draw square if ship is destroyed
                    shapesList.append(shapes.Rectangle(x2 + 10, y2 + 10, entryWidth - 20, entryHeight - 20, color, batch = batch))
                else:
                    # Draw cross
                    shapesList.append(shapes.Line(x2, y2, x2 + entryWidth, y2 + entryHeight, 1, color, batch = batch))
                    shapesList.append(shapes.Line(x2 + entryWidth, y2, x2, y2 + entryHeight, 1, color, batch = batch))

    # Draw the batch
    batch.draw()

def drawLabels():
    if(socket.getWinner() is not None):
        label = pyglet.text.Label( socket.getWinner() + " won!",
                font_name='Arial',
                font_size=36,
                x=window.width//2, y=window.height//2,
                anchor_x='center', anchor_y='center')
                
        label.draw()

pyglet.clock.schedule_interval(drawElements, 1/30.0)
pyglet.app.run()