socket.on("collabo", function (room) {
  socket.emit("create or join", room);
  console.log("Attempted to create or join room", room);
});
  
socket.on("connect", function () {
  socket.emit("onCollabo", socket.id);
});

socket.on("create or join", function (room) {
  log("Received request to create or join room " + room);
  var clientsInRoom = io.sockets.adapter.rooms[room];
  var numClients = clientsInRoom
    ? Object.keys(clientsInRoom.sockets).length
    : 0;
  log("Room " + room + " now has " + numClients + " client(s)");
  if (numClients === 0) {
    socket.join(room);
    log("Client ID " + socket.id + " created room " + room);
    socket.emit("created", room, socket.id);
  } else if (numClients === 1) {
    log("Client ID " + socket.id + " joined room " + room);
    io.sockets.in(room).emit("join", room);
    socket.join(room);
    socket.emit("joined", room, socket.id);
    io.sockets.in(room).emit("ready", room);
    socket.broadcast.emit("ready", room);
  } else {
    // max two clients
    socket.emit("full", room);
  }
});
