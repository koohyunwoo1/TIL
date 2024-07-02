import "./App.css";
import Viewer from "./components/Viewer";
import Controller from "./components/Countroller";
import { useState, useEffect } from "react";

function App() {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState("");

  useEffect(() => {
    console.log(`count : ${count} / input : ${input}`);
  }, [count, input]);

  // 배열에 입력된 값이 바뀔때마다, 콜백함수가 실행이된다.
  // 말 그대로 count가 바뀔때마다, setCount가 실행

  const onClickButton = (value) => {
    setCount(count + value);
  };

  return (
    <div className="App">
      <h1>Simple Counter</h1>
      <section>
        <input
          value={input}
          onChange={(e) => {
            setInput(e.target.value);
          }}
        />
      </section>
      <section>
        <Viewer count={count} />
      </section>
      <section>
        <Controller onClickButton={onClickButton} />
      </section>
    </div>
  );
}

export default App;
