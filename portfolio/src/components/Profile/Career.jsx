import React from "react";
import "../../style/Profile/Career.css";
import "../../style/Profile/Profile.css";

const Career = () => {
  return (
    <>
      <div className="Career">
        <i
          className="fas fa-project-diagram"
          style={{ marginRight: "10px" }}
        ></i>
        Career
      </div>
      <ul className="CareerTitle">
        <li className="CareerText">
          삼성청년SW아카데미 11th ( 2024.01 ~ 2024.12 )
          <ul className="CareerSubText">
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
      <div className="Career">
        <i
          className="fas fa-project-diagram"
          style={{ marginRight: "10px" }}
        ></i>
        Education
      </div>

      <ul className="CareerTitle">
        <li className="CareerText">
          경성대학교 빅데이터응용통계학과 (2018.03 ~ 2024.02)
          <ul className="CareerSubText">
            <li>
              SPSS 통계 프로그램을 사용하여 데이터 분석에 필요한 기초 통계 및
              다양한 분석 기법을 배웠습니다. 특히, 회귀 분석과 상관 분석을 통해
              데이터 간의 관계를 파악하는 방법을 익혔습니다.
            </li>
            <li>
              더불어, 여론조사 방법론을 배우고 실제 설문을 실시하여 수집한
              데이터를 분석하는 경험도 쌓았습니다.
            </li>
            <li>
              파이썬을 활용하여 타이타닉 데이터와 꽃잎 데이터셋을
              분석해보았습니다. 이 과정에서 데이터 전처리, 시각화, 통계적 분석
              등을 경험하며 실무적인 데이터 분석 능력을 키웠습니다.
            </li>
          </ul>
        </li>
      </ul>
    </>
  );
};

export default Career;
