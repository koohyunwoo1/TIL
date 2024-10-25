const WebSocket = require("ws");
const { v4: uuidv4 } = require("uuid");

const wss = new WebSocket.Server({ port: 8080 });
let connectedClients = 0;
let chatHistory = [];

wss.on("connection", (ws) => {
  connectedClients++;
  const userId = uuidv4();
  console.log(`유저 연결: ${userId}, 현재 연결된 유저 수: ${connectedClients}`);

  ws.send(JSON.stringify({ type: "assignUserId", userId }));
  ws.send(JSON.stringify({ type: "chatHistory", messages: chatHistory }));

  broadcast({ type: "userCount", count: connectedClients });

  ws.on("message", (message) => {
    const parsedMessage = JSON.parse(message);

    if (parsedMessage.type === "clearMessages") {
      chatHistory = [];
      console.log("채팅 기록이 삭제되었습니다.");

      broadcast({ type: "chatHistory", messages: chatHistory });
      return;
    }

    const { id, userId, message: msg } = parsedMessage;
    console.log(`${userId}: ${msg}`);

    const newMessage = { id, userId, message: msg };
    chatHistory.push(newMessage);

    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify(newMessage));
      }
    });
  });

  ws.on("close", () => {
    connectedClients--;
    console.log(
      `유저 끊김: ${userId}, 현재 연결된 유저 수: ${connectedClients}`
    );
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
