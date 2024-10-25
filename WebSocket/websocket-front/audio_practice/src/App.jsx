import { useEffect, useState } from "react";
import { v4 as uuidv4 } from "uuid";
import "./App.css";

const App = () => {
  const [socket, setSocket] = useState(null);
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState(() => {
    const savedMessages = localStorage.getItem("messages");
    return savedMessages ? JSON.parse(savedMessages) : [];
  });
  const [userCount, setUserCount] = useState(0);
  const [userId, setUserId] = useState(sessionStorage.getItem("userId"));

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8080");

    ws.onopen = () => {
      console.log("웹소켓 연결");
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      handleMessage(data);
    };

    setSocket(ws);

    return () => {
      ws.close();
    };
  }, []);

  const handleMessage = (data) => {
    if (data.type === "assignUserId") {
      if (!userId) {
        setUserId(data.userId);
        sessionStorage.setItem("userId", data.userId);
      }
    } else if (data.type === "userCount") {
      setUserCount(data.count);
    } else if (data.type === "chatHistory") {
      setMessages(data.messages);
      localStorage.setItem("messages", JSON.stringify(data.messages));
    } else {
      const { id, userId, message: msg } = data;
      const newMessage = { id, userId, msg };
      setMessages((prevMessages) => {
        const updatedMessages = [...prevMessages, newMessage];
        localStorage.setItem("messages", JSON.stringify(updatedMessages));
        return updatedMessages;
      });
    }
  };

  const sendMessage = () => {
    if (!userId || !message.trim()) return;
    const id = uuidv4();
    const payload = { id, userId, message };
    socket.send(JSON.stringify(payload));
    setMessage("");
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      sendMessage();
    }
  };

  const clearMessages = () => {
    setMessages([]);
    localStorage.removeItem("messages");
    socket.send(JSON.stringify({ type: "clearMessages" }));
  };

  return (
    <div className="container">
      <div className="header">
        <h1>채팅</h1>
        <h2>현재 인원: {userCount}</h2>
      </div>

      <div className="messageContainer">
        <div id="messages">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${
                msg.userId === userId ? "sent" : "received"
              }`}
            >
              <strong>{msg.userId}:</strong> {msg.msg}
            </div>
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="메세지 입력"
          />
          <button onClick={sendMessage} disabled={!userId}>
            전송
          </button>
          <button onClick={clearMessages}>전체 메세지 삭제</button>
        </div>
      </div>
    </div>
  );
};

export default App;
