import pyglet, sys
from pyglet import shapes

from __map import *
from __ship import *
from __socket import *

batch = pyglet.graphics.Batch()


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
map = Map(sizes)
socket = Socket('https://python.darrellvs.nl')

# Connect the websocket to the server
socket.connect();

# Create a pyglet window and eventloop
window = pyglet.window.Window(1000, 500)
eventLoop = pyglet.app.EventLoop()

# State of ship placement
placingFinished = False


# Window event handlers
@window.event
def on_draw():
    window.clear()
    drawGrid()

@window.event
def on_mouse_motion(x, y, dx, dy):
    return

@window.event
def on_mouse_press(x, y, button, modifiers):
    if(placingFinished):
        print(map.getEntry(x, y))

@window.event
def on_close():
    window.close()
    socket.disconnect()
    print('Running services closed successfully, exiting...')



def drawGrid():
    entryWidth = sizes['gridEntry']['width']
    entryHeight = sizes['gridEntry']['height']

    # For each grid item width
    for i in range(sizes['mapGrid']['width'] - 1):
        x = round(i * entryWidth + entryWidth);
        lines['horizontal'][i] = shapes.Line(x, 0, x, sizes['window']['height'], 1, (150, 150, 150), batch = batch)

    # For each grid item height
    for i in range(sizes['mapGrid']['height'] - 1):
        y = round(i * entryHeight + entryHeight);
        lines['vertical'][i] = shapes.Line(0, y, sizes['window']['width'], y, 1, (150, 150, 150), batch = batch)

    batch.draw()



pyglet.app.run()