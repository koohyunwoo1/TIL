// src/App.js

import React from "react";
import "./App.css";
import AvatarEditorComponent from "./components/AvatarEditor";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Create Your Avatar</h1>
        <AvatarEditorComponent />
      </header>
    </div>
  );
}

export default App;
