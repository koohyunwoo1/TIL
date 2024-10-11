import React from "react";
import GflexImage from "../../assets/Gflex.png";
import PillSooImage from "../../assets/PillSoo.png";
import RunUsImage from "../../assets/RunUs.png";
import "../../style/Project/ProjectItem.css";

const ProjectItem = () => {
  return (
    <div className="ProjectItem">
      <a
        href="https://github.com/koohyunwoo1/G-flex"
        target="_blank"
        rel="noopener noreferrer"
        className="ProjectLink"
      >
        <div className="ProjectCard">
          <img src={GflexImage} alt="Gflex" />
          {/* <h1>Gflex</h1> */}
        </div>
        {/* <p>기분/무드별 영화 추천 서비스입니다.</p> */}
      </a>
      <a
        href="https://github.com/koohyunwoo1/PillSoo"
        target="_blank"
        rel="noopener noreferrer"
        className="ProjectLink"
      >
        <div className="ProjectCard">
          <img src={PillSooImage} alt="PillSoo" />
          {/* <h1>PillSoo</h1> */}
        </div>
        {/* <p>사용자 기반 영양제 추천 서비스입니다.</p> */}
      </a>
      <a
        href="https://github.com/koohyunwoo1/RunUs"
        target="_blank"
        rel="noopener noreferrer"
        className="ProjectLink"
      >
        <div className="ProjectCard">
          <img src={RunUsImage} alt="RunUs" />
          {/* <h1>RunUs</h1> */}
        </div>
        {/* <p>함께 뛰는 러닝 서비스입니다.</p> */}
      </a>
    </div>
  );
};

export default ProjectItem;
