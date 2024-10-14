import React, { useState, useEffect } from "react";
import HeaderBar from "../../components/Home/HeaderBar";
import ProjectItem from "../../components/Project/ProjectItem";
import "../../style/Project/Project.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "../../style/Home/Home.css";

import GflexImage from "../../assets/Gflex.png";
import RunUsImage from "../../assets/RunUs.png";
import PillSooImage from "../../assets/PillSoo.png";

const Project = () => {
  const [showHeaderBar, setShowHeaderBar] = useState(false);
  const [animateTitle, setAnimateTitle] = useState(false);
  const [showArrow, setShowArrow] = useState(false);

  const projects = [
    {
      title: "Gflex",
      image: GflexImage,
      description: "기분/무드별 영화 추천 서비스입니다.",
      link: "https://github.com/koohyunwoo1/G-flex",
    },
    {
      title: "RunUs",
      image: RunUsImage,
      description: "함께 뛰는 러닝 서비스입니다.",
      link: "https://github.com/koohyunwoo1/RunUs",
    },
    {
      title: "PillSoo",
      image: PillSooImage,
      description: "사용자 기반 영양제 추천 서비스입니다.",
      link: "https://github.com/koohyunwoo1/PillSoo",
    },
  ];

  const handleArrowClick = () => {
    const projectSubtitleElement = document.getElementById("project-subtitle");
    if (projectSubtitleElement) {
      projectSubtitleElement.scrollIntoView({ behavior: "smooth" });
    }
  };

  const handleScroll = () => {
    const projectItemElement = document.getElementById("project-item");
    if (projectItemElement) {
      const rect = projectItemElement.getBoundingClientRect();
      setShowHeaderBar(rect.top <= window.innerHeight && rect.bottom >= 0);
    }
  };

  useEffect(() => {
    window.scrollTo(0, 0);
    window.addEventListener("scroll", handleScroll);
    setAnimateTitle(true);

    const timer = setTimeout(() => {
      setShowArrow(true);
    }, 1000);

    return () => {
      window.removeEventListener("scroll", handleScroll);
      clearTimeout(timer);
    };
  }, []);

  return (
    <div className="Project">
      {showHeaderBar && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            zIndex: 1000,
            width: "80%",
            margin: "0 auto",
            transition: "opacity 0.3s ease",
            opacity: showHeaderBar ? 1 : 0,
          }}
        >
          <HeaderBar />
        </div>
      )}
      <div className={`ProjectTitle ${animateTitle ? "fade-in" : ""}`}>
        <i
          className="fas fa-project-diagram"
          style={{ marginRight: "10px" }}
        ></i>
        Projects
      </div>
      {showArrow && (
        <div
          className="arrow"
          onClick={handleArrowClick}
          style={{
            position: "absolute",
            bottom: "150px",
            left: "50%",
          }}
        >
          <span></span>
          <span></span>
        </div>
      )}
      <div className="ProjectSubtitle" id="project-subtitle">
        <i className="fas fa-check-circle" style={{ marginRight: "10px" }}></i>
        나의 프로젝트
      </div>
      <div className="ProjectSubtitle2">
        {projects.length}개의 프로젝트를 진행하였습니다. 아래에서 자세한 내용을
        확인하세요.
      </div>
      <div className="ProjectItemContainer" id="project-item">
        <ProjectItem projects={projects} />
      </div>
    </div>
  );
};

export default Project;
