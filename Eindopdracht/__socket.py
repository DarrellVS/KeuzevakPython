import socketio

class Socket:
    def __init__(self, host):
        self.host = host
        self.sio = socketio.Client()

        @self.sio.event
        def connect():
            print('Websocket connected to server @', self.host)

        # Upon receiving a message with label bruhtering
        @self.sio.on('bruhtering')
        def on_message(data):
            print('I received a message!')

    def connect(self):
        self.sio.connect(self.host)

    def disconnect(self):
        self.sio.disconnect()