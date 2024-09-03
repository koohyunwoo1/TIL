// Box.js
import React, { useState } from "react";
import "../styles/Box.css";

const Box = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleLid = () => {
    setIsOpen((prevState) => !prevState);
  };

  return (
    <div className="box">
      <div className={`lid ${isOpen ? "open" : ""}`}></div>
      <div className="content">
        <div className="cross">
          <div className="horizontal"></div>
          <div className="vertical"></div>
        </div>
        <div className="label">First Aid</div>
      </div>
      <button onClick={toggleLid} className="toggle-button">
        {isOpen ? "Close Lid" : "Open Lid"}
      </button>
    </div>
  );
};

export default Box;
