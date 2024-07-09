// src/components/AnimatedComponent.js
import React, { useState } from "react";
import "animate.css";

const AnimatedComponent = () => {
  const [isAnimating, setIsAnimating] = useState(false);
  const [showSecondAnimation, setShowSecondAnimation] = useState(false);

  const handleClick = () => {
    setIsAnimating(true);
    setTimeout(() => {
      setIsAnimating(false); // 첫 번째 애니메이션 종료 후 상태 변경
      setShowSecondAnimation(true); // 두 번째 애니메이션 시작
    }, 1000); // 'bounceOut' 애니메이션 지속 시간 (1초)
  };

  return (
    <div>
      <h1
        onClick={handleClick}
        className={`animate__animated ${
          isAnimating ? "animate__bounceOut" : ""
        }`} // 첫 번째 h1 태그
      >
        An animated element
      </h1>
      <h2
        className={`animate__animated ${
          showSecondAnimation ? "animate__bounceIn" : ""
        }`} // 두 번째 h2 태그
      >
        두두등장
      </h2>
    </div>
  );
};

export default AnimatedComponent;
