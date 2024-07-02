import "./App.css";
import Viewer from "./components/Viewer";
import Controller from "./components/Countroller";
import { useState, useEffect, useRef } from "react";
import Even from "./components/Even";

function App() {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState("");

  const isMount = useRef(false);

  // 1. 마운트 : 탄생
  useEffect(() => {
    console.log("mount");
  }, []);
  // 2. 업데이트 : 변화, 리렌더링
  useEffect(() => {
    if (!isMount.current) {
      isMount.current = true;
      return;
    }
    // 처음에 console.log("update")가 마운트 되지 않고
    // 버튼을 클릭시에 update가 콘솔창에 출력된다.
    console.log("update");
  });
  // 3. 언마운트 : 죽음

  // Even.jsx
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
        {count % 2 === 0 ? <Even /> : null}
        {/* 짝수 일때는 Even 컴포넌트가 출력되고 */}
        {/* 아니면 아무것도 출력되지 않게 한다. */}
      </section>
      <section>
        <Controller onClickButton={onClickButton} />
      </section>
    </div>
  );
}

export default App;
