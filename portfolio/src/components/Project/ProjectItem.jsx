import React, { Component } from "react";
import { FaGithub } from "react-icons/fa";
import "../../style/Project/ProjectItem.css";

import GflexThumbnail from "../../assets/Gflex.png";
import PillSooThumbnail from "../../assets/PillSoo.png";
import RunUsThumbnail from "../../assets/RunUs.png";

const projects = [
  {
    id: 1,
    title: "Gflex",
    thumbnail: GflexThumbnail,
    images: Array.from(
      { length: 12 },
      (_, index) => `/assets/Gflex/image${index}.png`
    ),
    period: "2024.05.16 - 2024.05.24 (1주)",
    link: "https://github.com/koohyunwoo1/G-flex",
  },
  {
    id: 2,
    title: "RunUs",
    thumbnail: RunUsThumbnail,
    images: Array.from(
      { length: 12 },
      (_, index) => `/assets/RunUs/image${index}.gif`
    ),
    period: "2024.07.05 - 2024.08.16 (6주)",
    link: "https://github.com/koohyunwoo1/RunUs",
  },
  {
    id: 3,
    title: "PillSoo",
    thumbnail: PillSooThumbnail,
    images: Array.from(
      { length: 12 },
      (_, index) => `/assets/PillSoo/image${index}.jpg`
    ),
    period: "2024.08.26 - 2024.10.11 (7주)",
    link: "https://github.com/koohyunwoo1/PillSoo",
  },
];

class ProjectItem extends Component {
  state = {
    selectedProject: null,
  };

  openModal = (project) => {
    this.setState({ selectedProject: project });
  };

  closeModal = () => {
    this.setState({ selectedProject: null });
  };

  render() {
    return (
      <div className="projectItem">
        {projects.map((project) => (
          <div
            key={project.id}
            className="projectCard"
            onClick={() => this.openModal(project)}
          >
            <img
              src={project.thumbnail}
              alt={project.title}
              className="projectImage"
            />
            <div className="projectDetails">
              <h1>{project.title}</h1>
              <p className="projectPeriod">{project.period}</p>
            </div>
          </div>
        ))}

        {this.state.selectedProject && (
          <div className="modal" onClick={this.closeModal}>
            <div className="modalContent" onClick={(e) => e.stopPropagation()}>
              <span className="modalClose" onClick={this.closeModal}>
                &times;
              </span>
              <div className="modalHeader">
                <h2 style={{ color: "white", marginLeft: "20px" }}>
                  {this.state.selectedProject.title}
                </h2>
                <a
                  href={this.state.selectedProject.link}
                  className="githubButton"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <FaGithub style={{ fontSize: "24px" }} /> GitHub
                </a>
              </div>
              <div className="projectDetail">
                <p className="projectPeriod">
                  {this.state.selectedProject.period}
                </p>
                <div className="projectSkills">
                  <h1>Skills</h1>
                  <div>
                    {this.state.selectedProject.title === "Gflex" ? (
                      <>
                        <span className="projectBadge">Django</span>
                        <span className="projectBadge">Vue.js</span>
                      </>
                    ) : this.state.selectedProject.title === "RunUs" ? (
                      <>
                        <span className="projectBadge">React.js</span>
                        <span className="projectBadge">Spring</span>
                      </>
                    ) : (
                      <>
                        <span className="projectBadge">ReactNative</span>
                        <span className="projectBadge">Spring</span>
                      </>
                    )}
                  </div>
                </div>

                <div className="projectTools">
                  <h1>Tools</h1>
                  <div>
                    {this.state.selectedProject.title === "Gflex" ? (
                      <span className="projectBadge">Visual Studio</span>
                    ) : (
                      <>
                        <span className="projectBadge">Visual Studio</span>
                        <span className="projectBadge">MySQL</span>
                      </>
                    )}
                  </div>
                </div>

                <div className="projectTeam">
                  <h1>개발 인원</h1>
                  <p>
                    {this.state.selectedProject.title === "Gflex"
                      ? "2명 (백엔드 1명, 프론트엔드 1명)"
                      : this.state.selectedProject.title === "RunUs"
                      ? "7명 (백엔드 5명, 프론트엔드 2명)"
                      : "6명 (백엔드 4명, 프론트엔드 2명)"}
                  </p>
                </div>
                <div className="projectRole">
                  <h1>역할</h1>
                  <p>
                    {this.state.selectedProject.title === "Gflex"
                      ? "기획, 프론트엔드, 백엔드"
                      : this.state.selectedProject.title === "RunUs"
                      ? "기획, 전체적인 UI 담당, Auth 기능 제외 모든 기능 담당, Geolocation API를 사용해서 위치 튐 현상 보정"
                      : "기획, 전체적인 UI 담당, Auth 기능, API 연동"}
                  </p>
                </div>
                <div className="projectDescription">
                  <h1>프로젝트 설명</h1>
                  <p>
                    {this.state.selectedProject.title === "Gflex"
                      ? "Gflex는 검색을 통한 영화 추천 서비스 , 장르 및 무드에 따른 영화 추천 서비스를 제공 하는 프로젝트입니다 !"
                      : this.state.selectedProject.title === "RunUs"
                      ? "RunUs는..."
                      : "PillSoo는..."}
                  </p>
                </div>
              </div>
              <div className="projectImages">
                {this.state.selectedProject.images.map((image, index) => (
                  <img key={index} src={image} alt={`project ${index}`} />
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    );
  }
}

export default ProjectItem;
