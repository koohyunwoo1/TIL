import { useEffect, useState } from "react";
import { v4 as uuidv4 } from "uuid";
import "./App.css"; // CSS 파일 경로가 맞는지 확인하세요.

const App = () => {
  const [socket, setSocket] = useState(null);
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [userCount, setUserCount] = useState(0);
  const clientId = uuidv4();
  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8080");

    ws.onopen = () => {
      console.log("웹소켓 연결");
    };

    ws.onmessage = (event) => {
      if (event.data instanceof Blob) {
        const reader = new FileReader();
        reader.onload = () => {
          const data = JSON.parse(reader.result);
          handleMessage(data);
        };
        reader.readAsText(event.data);
      } else {
        const data = JSON.parse(event.data);
        handleMessage(data);
      }
    };

    setSocket(ws);

    return () => {
      ws.close();
    };
  }, []);

  const handleMessage = (data) => {
    if (data.type === "userCount") {
      setUserCount(data.count);
    } else {
      const { id, message: msg } = data;
      setMessages((prevMessages) => [...prevMessages, { id, msg }]);
    }
  };

  const sendMessage = () => {
    const payload = { id: clientId, message: message };
    socket.send(JSON.stringify(payload));
    setMessage("");
  };

  return (
    <div className="any">
      <h1>Chat App</h1>
      <h2>현재 사용자 수: {userCount}</h2>
      <div id="messages">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.id === clientId ? "sent" : "received"}`}
          >
            <strong>{msg.id}:</strong> {msg.msg}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="메세지 입력"
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default App;
