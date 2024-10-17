import React from "react";
import "../../style/Profile/Carrer.css";
import "../../style/Profile/Profile.css";

const Carrer = () => {
  return (
    <>
      <div className="Carrer">
        <i
          className="fas fa-project-diagram"
          style={{ marginRight: "10px" }}
        ></i>
        Carrer
      </div>
      <ul className="CarrerTitle">
        <li className="CarrerText">
          삼성청년SW아카데미 11th ( 2024.01 ~ 2024.12 )
          <ul className="CarrerSubText">
            <li>
              파이썬 반에서 시작하여 파이썬을 이용해 Django 프레임워크를
              학습했습니다. 이 과정에서 HTML과 CSS와 같은 웹 기본 기술을 익혔고,
              JavaScript 교육을 통해 프론트엔드 프레임워크인 Vue.js를
              배웠습니다.
            </li>
            <li>
              2학기에는 두 번의 프로젝트 경험을 통해 React를 새롭게 배우게
              되었으며, 더 나아가 TypeScript를 사용하여 React Native로 모바일
              애플리케이션을 개발한 경험이 있습니다. 이러한 프로젝트 경험을 통해
              프론트엔드와 백엔드 전반에 걸친 개발 역량을 키웠습니다.
            </li>
          </ul>
        </li>
      </ul>
      <hr className="ProfileHr" />
      <div className="Carrer">
        <i
          className="fas fa-project-diagram"
          style={{ marginRight: "10px" }}
        ></i>
        Education
      </div>

      <ul className="CarrerTitle">
        <li className="CarrerText">
          경성대학교 빅데이터응용통계학과 ( 2018.03 ~ 2024.02 )
          <ul className="CarrerSubText">
            <li>자세한 내용</li>
          </ul>
        </li>
      </ul>
    </>
  );
};

export default Carrer;
