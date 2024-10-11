import React from "react";
import HeaderBar from "../../components/Home/HeaderBar";
import ProjectItem from "../../components/Project/ProjectItem";
import "../../style/Project/Project.css";

const Project = () => {
  return (
    <div className="Project">
      <div>
        <HeaderBar />
      </div>
      <div className="ProjectTitle">Projects</div>
      <div className="ProjectItemContainer">
        <ProjectItem />
      </div>
    </div>
  );
};

export default Project;
