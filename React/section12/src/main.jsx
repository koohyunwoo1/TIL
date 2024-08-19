import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { BrowserRouter } from "react-router-dom";
ReactDOM.createRoot(document.getElementById("root")).render(
  // HTML5의 History API를 사용하여 페이지를 새로 고침하지 않아도
  // URL을 업데이트하고, 브라우저의 뒤로 가기, 및 앞으로 기능을 할 수 있게 된다.
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
