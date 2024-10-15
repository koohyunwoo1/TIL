import React, { Component } from "react";
import Slider from "react-slick";
import "../../style/Project/ProjectItem.css";

const projects = [
  {
    title: "Gflex",
    images: Array.from(
      { length: 12 },
      (_, index) => `/assets/Gflex/image${index}.png`
    ),
    description: "기분/무드별 영화 추천 서비스입니다.",
    period: "2023.01 - 2023.06",
    link: "https://github.com/koohyunwoo1/G-flex",
  },
  {
    title: "PillSoo",
    images: Array.from(
      { length: 12 },
      (_, index) => `/assets/PillSoo/image${index}.jpg`
    ),
    description: "사용자 기반 영양제 추천 서비스입니다.",
    period: "2023.01 - 2023.06",
    link: "https://github.com/koohyunwoo1/PillSoo",
  },
  {
    title: "RunUs",
    images: Array.from(
      { length: 12 },
      (_, index) => `/assets/RunUs/image${index}.gif`
    ),
    description: "함께 뛰는 러닝 서비스입니다.",
    period: "2023.07 - 2023.12",
    link: "https://github.com/koohyunwoo1/RunUs",
  },
];

class ProjectItem extends Component {
  render() {
    const settings = {
      dots: false,
      infinite: true,
      speed: 500,
      slidesToShow: 3,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 2000,
      cssEase: "ease-in-out",
    };

    return (
      <div className="projectItem">
        {projects.map((project) => (
          <div key={project.title} className="projectCard">
            <h2>{project.title}</h2>
            <p className="projectPeriod">{project.period}</p>
            <div className="carousel">
              <Slider {...settings}>
                {project.images.map((image, index) => (
                  <div key={index} className="carouselImage">
                    <img src={image} alt={`${project.title} ${index}`} />
                  </div>
                ))}
              </Slider>
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
  }
}

export default ProjectItem;
