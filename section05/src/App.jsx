import "./App.css";
import { useState } from "react";
// 확장자는 굳이 안써도됨.

// 부모 컴포넌트
function App() {
  const [state, setState] = useState(0);
  return (
    <>
      <h1>{state}</h1>
      <button
        onClick={() => {
          setState(state + 1);
        }}
      ></button>
    </>
  );
}

export default App;
