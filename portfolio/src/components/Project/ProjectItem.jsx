import React from "react";
import GflexImage from "../../assets/Gflex.png";
import PillSooImage from "../../assets/PillSoo.png";
import RunUsImage from "../../assets/RunUs.png";
import "../../style/Project/ProjectItem.css";

const ProjectItem = () => {
  const projects = [
    {
      title: "Gflex",
      image: GflexImage,
      description: "기분/무드별 영화 추천 서비스입니다.",
      period: "2023.01 - 2023.06",
      link: "https://github.com/koohyunwoo1/G-flex",
    },
    {
      title: "RunUs",
      image: RunUsImage,
      description: "함께 뛰는 러닝 서비스입니다.",
      period: "2023.07 - 2023.12",
      link: "https://github.com/koohyunwoo1/RunUs",
    },
    {
      title: "PillSoo",
      image: PillSooImage,
      description: "사용자 기반 영양제 추천 서비스입니다.",
      period: "2023.01 - 2023.06",
      link: "https://github.com/koohyunwoo1/PillSoo",
    },
  ];

  return (
    <div className="projectItem">
      {projects.map((project) => (
        <div key={project.title} className="projectCard">
          <h2>{project.title}</h2>
          <p className="projectPeriod">{project.period}</p>
          <div className="carousel">
            <img src={project.image} alt={project.title} />
          </div>
          <div className="projectDescription">
            <p>{project.description}</p>
            <a
              href={project.link}
              target="_blank"
              rel="noopener noreferrer"
              className="modalLink"
            >
              GitHub 링크
            </a>
          </div>
        </div>
      ))}
    </div>
  );
};

export default ProjectItem;
