import socketio
from __map import *

class Socket:
    def __init__(self, host, myMap, sizes):
        self.host = host                    # Host to which to connect 
        self.sio = socketio.Client()        # Socket IO Client
        self.sizes = sizes                  # Sizes dictionary
        self.opponentMap = None             # The opponent's map
        self.myMap = myMap                  # Holds tha player's map
        self.winner = None                  # Holds the winner of the game
        self.semafore = False;           # Keep track of playing order

        # Connection event
        @self.sio.event
        def connect():
            print('Websocket connected to server @', self.host)

        # Upon receiving the opponent map
        @self.sio.on('shareable-matrix')
        def on_message(shareableMatrix):
            m = Map(self.sizes)
            self.opponentMap = m.getMatrixFromOpponentMap(shareableMatrix)

        # The opponent destoryed one of your ships // Remove it from your map
        @self.sio.on('destroy-ship')
        def on_message(index):
            entry = myMap.getEntry(index[0], index[1])
            self.myMap.destroyShip(entry)

        # The opponent wins
        @self.sio.on('opponent-wins')
        def on_message():
            self.winner = 'Opponent'

        # Upon receiving the semafore
        @self.sio.on('semafore')
        def on_message():
            self.semafore = True

    # Connect to the host (socket io server) 
    def connect(self):
        self.sio.connect(self.host)

    # Disconnect from the host
    def disconnect(self):
        self.sio.disconnect()

    # Send a finnished placement event, passed to the opponent over the server
    def finishedPlacement(self, shareableMatrix):
        self.sio.emit('finished-placement', shareableMatrix)

    # Destroy an opponent's ship
    def destroyOpponentShip(self, index):
        self.sio.emit('destroy-opponent-ship', index)

    # Emit event upon game win
    def win(self):
        self.winner = 'You'             # You have won
        self.sio.emit('player-wins')    # Emit an event to the socket io server

    def sendSemafore(self):
        self.semafore = False
        self.sio.emit('semafore')

    # Return the opponent's map
    def getOpponentMap(self):
        return self.opponentMap

    # Return the winner variable
    def getWinner(self):
        return self.winner

    def hasSemafore(self):
        return self.semafore