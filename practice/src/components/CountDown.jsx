import React, { useState, useEffect } from "react";
import "../styles/CountDown.css";

const CountDown = () => {
  const [countdown, setCountdown] = useState(0);

  const handleClick = () => {
    setCountdown(3);
  };

  useEffect(() => {
    if (countdown === 0) return;
    const timer = setInterval(() => {
      setCountdown((prevCount) => prevCount - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [countdown]);

  return (
    <div className={`container3 ${countdown > 0 ? "active" : ""}`}>
      {countdown === 0 && (
        <button onClick={handleClick}>Start Countdown</button>
      )}
      {countdown > 0 && <div className="countdown">{countdown}</div>}
    </div>
  );
};

export default CountDown;
