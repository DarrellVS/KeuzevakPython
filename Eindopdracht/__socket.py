import socketio
from __map import *

class Socket:
    def __init__(self, host, myMap, sizes):
        self.host = host
        self.sio = socketio.Client()
        self.opponentMap = None
        self.sizes = sizes
        self.opponentMapRetreived = False;
        self.myMap = myMap

        @self.sio.event
        def connect():
            print('Websocket connected to server @', self.host)

        # Upon receiving a message with label bruhtering
        @self.sio.on('shareable-matrix')
        def on_message(shareableMatrix):
            m = Map(self.sizes);
            self.opponentMap = m.getMatrixFromOpponentMap(shareableMatrix);

        @self.sio.on('destroy-ship')
        def on_message(index):
            print('Destroying ship @ ', index)
            entry = myMap.getEntry(index[0], index[1])
            print(entry)
            self.myMap.destroyShip(entry)

    def connect(self):
        self.sio.connect(self.host)

    def disconnect(self):
        self.sio.disconnect()

    def finishedPlacement(self, shareableMatrix):
        self.sio.emit('finished-placement', shareableMatrix)

    def destroyOpponentShip(self, index):
        self.sio.emit('destroy-opponent-ship', index)

    def getOpponentMap(self):
        return self.opponentMap