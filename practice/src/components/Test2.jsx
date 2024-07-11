// Test2.jsx
import React, { useState, useEffect } from "react";
import "../styles/Test2.css";

const Test2 = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [startTime, setStartTime] = useState(null);
  const [elapsedTime, setElapsedTime] = useState(0);

  useEffect(() => {
    let intervalId;

    if (startTime) {
      intervalId = setInterval(() => {
        const now = Date.now();
        setElapsedTime(now - startTime);
      }, 100);
    } else {
      clearInterval(intervalId);
      setElapsedTime(0);
    }

    return () => clearInterval(intervalId);
  }, [startTime]);

  const handleSingleRunClick = () => {
    setStartTime(Date.now());
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setStartTime(null);
    setElapsedTime(0);
  };

  const handleModalClickOutside = (e) => {
    if (e.target.classList.contains("modal")) {
      handleCloseModal();
    }
  };

  return (
    <div className="test2">
      <button className="run-button single-run" onClick={handleSingleRunClick}>
        혼자 뛰시겠습니까 ?
      </button>
      <button className="run-button group-run">함께 뛰시겠습니까 ?</button>

      {isModalOpen && (
        <div className="modal" onClick={handleModalClickOutside}>
          <div className="modal-content">
            <span className="close" onClick={handleCloseModal}>
              &times;
            </span>
            <p>경과 시간: {Math.floor(elapsedTime / 1000)} 초</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default Test2;
