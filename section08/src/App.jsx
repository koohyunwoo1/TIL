import "./App.css";
import Editor from "./components/Editor";
import Header from "./components/Header";
import List from "./components/List";
import { useState, useRef } from "react";

// 임시데이터
const mockData = [
  {
    id: 0,
    isDone: false,
    content: "React 공부하기",
    date: new Date().getTime(),
  },
  {
    id: 1,
    isDone: false,
    content: "빨래하기",
    date: new Date().getTime(),
  },
  {
    id: 2,
    isDone: false,
    content: "노래 연습하기",
    date: new Date().getTime(),
  },
];

// state를 만드는 모든 것은 App.jsx에 만들면 된다.
function App() {
  const [todos, setTodos] = useState(mockData);
  const idRef = useRef(3);
  // todos를 추가할려면 setTodos 함수가 실행이 되어야한다.
  // state는 setTodos같은 상태변환 함수로만 변경할수있다.
  const onCreate = (content) => {
    const newTodo = {
      id: idRef.current++,
      isDone: false,
      content: content,
      date: new Date().getTime(),
    };

    // 이 객체를 todos배열에 추가해줘야한다.
    setTodos([newTodo, ...todos]);
    // 기존에 있는 todos 배열
  };

  return (
    <div className="App">
      <Header />
      <Editor onCreate={onCreate} />
      <List todos={todos} />
    </div>
  );
}

export default App;
