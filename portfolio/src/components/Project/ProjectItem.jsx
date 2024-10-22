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
                      ? "기획, 프론트엔드, 백엔드(Django) 담당"
                      : this.state.selectedProject.title === "RunUs"
                      ? "기획, 전체적인 UI 담당, Auth 기능을 제외한 모든 기능 개발. Geolocation API를 사용하여 위치 정보를 받아오고, 알고리즘을 활용해 위치 튐 현상을 보정"
                      : "기획, 전체적인 UI 담당, Auth 기능, REST API, OCR 분석 담당"}
                  </p>
                </div>
                <div className="projectDescription">
                  <h1>프로젝트 설명</h1>
                  <p>
                    {this.state.selectedProject.title === "Gflex"
                      ? "Gflex는 사용자의 검색을 기반으로 영화 추천을 제공하는 서비스입니다. 장르와 무드에 따라 맞춤형 영화 추천을 받을 수 있습니다."
                      : this.state.selectedProject.title === "RunUs"
                      ? "RunUs는 러닝을 시작하는 데 동기가 필요한 사람들을 위한 서비스입니다. 웹 소켓을 이용한 실시간 통신으로 함께 달리는 경험을 제공하는 앱입니다."
                      : "PillSoo는 바쁜 현대인들이 적절한 영양제를 선택할 수 있도록 돕는 서비스입니다. 연령대별로 맞춤형 영양제를 추천하고, 사용자의 현재 건강 상태를 입력하면 알맞은 영양제를 추천받을 수 있습니다."}
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
