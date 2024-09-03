import React, { useState, useEffect } from "react";
import "../styles/Box.css";

const Box = () => {
  const [isBubbleVisible, setIsBubbleVisible] = useState(false);

  const supplements = [
    "비타민 C",
    "오메가-3 피쉬 오일",
    "칼슘",
    "프로바이오틱",
    "마그네슘",
  ];

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsBubbleVisible(true);
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div style={{ marginTop: "500px" }}>
      <div className="box">
        <div className="lid open"></div>
        <div className="content">
          <div className="cross">
            <div className="horizontal"></div>
            <div className="vertical"></div>
          </div>
          <div className="label">My Kit</div>
        </div>
        <div className={`bubble ${isBubbleVisible ? "show" : ""}`}>
          {supplements.map((supplement, index) => (
            <p key={index}>{supplement}</p>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Box;
