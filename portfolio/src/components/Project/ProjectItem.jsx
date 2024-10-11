import React, { useState } from "react";
import GflexImage from "../../assets/Gflex.png";
import PillSooImage from "../../assets/PillSoo.png";
import RunUsImage from "../../assets/RunUs.png";
import "../../style/Project/ProjectItem.css";

const ProjectItem = () => {
  const [activeProject, setActiveProject] = useState(null);

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

  const handleProjectClick = (project) => {
    setActiveProject(project);
  };

  const closeModal = () => {
    setActiveProject(null);
  };

  const handleModalClick = (e) => {
    if (e.target.className === "modal") {
      closeModal();
    }
  };

  return (
    <div className="projectItem">
      {projects.map((project) => (
        <div key={project.title} onClick={() => handleProjectClick(project)}>
          <div className="projectCard">
            <img src={project.image} alt={project.title} />
          </div>
        </div>
      ))}

      {activeProject && (
        <div className="modal" onClick={handleModalClick}>
          <div className="modalContent">
            <span className="close" onClick={closeModal}>
              &times;
            </span>
            <h2>{activeProject.title}</h2>
            <p>{activeProject.description}</p>
            <a
              href={activeProject.link}
              target="_blank"
              rel="noopener noreferrer"
              className="modalLink"
            >
              GitHub 링크
            </a>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProjectItem;
