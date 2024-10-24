const WebSocket = require("ws");

const wss = new WebSocket.Server({ port: 8080 });
let connectedClients = 0;

wss.on("connection", (ws) => {
  connectedClients++;
  console.log("유저 연결", connectedClients);

  broadcast({ type: "userCount", count: connectedClients });

  ws.on("message", (message) => {
    console.log(`${message}`);
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });

  ws.on("close", () => {
    connectedClients--;
    console.log("유저 끊김", connectedClients);

    broadcast({ type: "userCount", count: connectedClients });
  });
});

function broadcast(data) {
  const message = JSON.stringify(data);
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(message);
    }
  });
}

console.log("서버 실행");
