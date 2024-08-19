import React, { useState, useEffect } from "react";
import "../styles/CountDown.css";

const CountDown = () => {
  const [countdown, setCountdown] = useState(0);
  const [key, setKey] = useState(0);

  const handleClick = () => {
    setCountdown(3);
    setKey((prevKey) => prevKey + 1);
  };

  useEffect(() => {
    if (countdown === 0) return;
    const timer = setInterval(() => {
      setCountdown((prevCount) => {
        if (prevCount === 1) {
          clearInterval(timer);
          return 0;
        }
        setKey((prevKey) => prevKey + 1);
        return prevCount - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [countdown]);

  return (
    <div className={`container3 ${countdown > 0 ? "active" : ""}`}>
      {countdown === 0 && (
        <button onClick={handleClick}>Start Countdown</button>
      )}
      {countdown > 0 && (
        <div className="countdown" key={key}>
          {countdown}
        </div>
      )}
    </div>
  );
};

export default CountDown;
