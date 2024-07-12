import React from "react";
import "../styles/Test4.css";
import { useInView } from "react-intersection-observer";

const Test4 = () => {
  const { ref, inView } = useInView({
    triggerOnce: true,
    threshold: 0.5,
  });

  return (
    <div ref={ref} className={`container2 ${inView ? "animate" : ""}`}>
      <div className="image3">
        <img src="src/assets/006.png" alt="" className="image image1" />
        {/* <img src="src/assets/007.png" alt="" className="image image2" /> */}
      </div>
      <div className="text3">
        <h1>꾸준히 기록하고</h1>
        <h1>건강한 습관을 만들어보세요 !</h1>
      </div>
    </div>
  );
};

export default Test4;
