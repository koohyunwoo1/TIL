import React, { useEffect } from "react";
import "../styles/Test3.css";
import { useInView } from "react-intersection-observer";

const Test3 = () => {
  const { ref, inView } = useInView({
    triggerOnce: true,
    threshold: 0.3,
  });

  useEffect(() => {
    if (inView) {
      document.querySelectorAll(".image").forEach((item, index) => {
        item.style.transitionDelay = `${index * 0.3}s`;
        item.classList.add("animate");
      });
    }
  }, [inView]);

  return (
    <div className="container">
      <div className="title-container">
        <div className="title2">
          <h1>시작이 어렵다면 ?</h1>
          <h1>작은 미션부터 시작해보세요</h1>
        </div>
        <div className="content" ref={ref}>
          <span>
            <img src="src/assets/004.png" alt="" className="image" />
          </span>
          <span>
            <img src="src/assets/005.png" alt="" className="image" />
          </span>
          <span>
            <img src="src/assets/005.png" alt="" className="image" />
          </span>
          <span>
            <img src="src/assets/004.png" alt="" className="image" />
          </span>
        </div>
      </div>
    </div>
  );
};

export default Test3;
