const cors = require('cors')
const path = require('path')
const http = require('http')
const express = require('express')

const app = express()
const server = http.createServer(app)
const io = require('socket.io')(server)

// Port on which the server listens
const port = 3012;

let clients = {}
let clientCount = 0;
const getOppositeClient = id => clients[Object.keys(clients).filter(c => c != id)[0]]

// Validation filter
io.use((socket, next) => clientCount <= 2 ? next() : next(new Error("Max concurrent connections reached")));

io.on('connection', (socket) => {
    console.log('New client connected');
    clients[socket.id] = { finishedPlacement: false, socket };
    clientCount++;

    // Pass the semafore to the first connecting client
    if(clientCount == 1) socket.emit('semafore')

    socket.on('disconnect', () => {
        clientCount--;
        delete clients[socket.id];

        console.log('Client disconnected')
    });

    socket.on('finished-placement', shareableMatrix => {
        clients[socket.id].finishedPlacement = true;
        clients[socket.id].shareableMatrix = shareableMatrix;
        console.log(`Received sharebleMatrix from client ${socket.id}`)

        const clts = Object.keys(clients)

        // Return if both parties did not complete their ship placement
        if (clts.filter(id => clients[id].finishedPlacement === true).length !== 2) return;

        // Send shareable matrix to each other
        clients[clts[0]].socket.emit('shareable-matrix', clients[clts[1]].shareableMatrix)
        clients[clts[1]].socket.emit('shareable-matrix', clients[clts[0]].shareableMatrix)
    })

    socket.on('destroy-opponent-ship', index => {
        getOppositeClient(socket.id).socket.emit('destroy-ship', index)
    })

    socket.on('semafore', () => getOppositeClient(socket.id).socket.emit('semafore'))

    socket.on('player-wins', () => getOppositeClient(socket.id).socket.emit('opponent-wins'))
})

app.set('trust proxy', true)
app.use(cors())

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'rick rolled.mp4'))
})

// Open the server on the port
server.listen(port, () => {
    console.log(`Socket.io server listening on ${port}`)
})