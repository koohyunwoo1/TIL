import React from "react";
import "../../style/Profile/Profile.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faUser,
  faBirthdayCake,
  faEnvelope,
  faCodeBranch,
} from "@fortawesome/free-solid-svg-icons";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
import { SiNotion } from "react-icons/si";
import Skill from "./Skill";
import Career from "./Career";

const Profile = () => {
  return (
    <div>
      <div className="Profile">
        <div className="ProfileImage" />
        <div className="ProfileDetails">
          <div className="ProfileName">
            <FontAwesomeIcon icon={faUser} /> 구현우
          </div>
          <div className="ProfileBirth">
            <FontAwesomeIcon icon={faBirthdayCake} /> 1999.07.07
          </div>
          <div className="ProfileEmailContainer">
            <FontAwesomeIcon icon={faEnvelope} />
            <a href="mailto:kjklovekhw@gmail.com" className="ProfileEmail">
              kjklovekhw@gmail.com
            </a>
          </div>

          <div className="Badges">
            <span className="Badge">
              <FontAwesomeIcon icon={faCodeBranch} /> Frontend Developer
            </span>
            <span className="Badge">React.js</span>
          </div>
          <div className="ProfileIntro">
            사용자 중심의 인터페이스를 만들어가는 프론트엔드 개발자입니다.
          </div>
          <div className="ProfileLink">
            <div className="ProfileGithub">
              <a
                href="https://github.com/koohyunwoo1"
                target="_blank"
                rel="noopener noreferrer"
              >
                <FontAwesomeIcon icon={faGithub} /> GitHub
              </a>
            </div>
            <div className="ProfileNotion">
              <a
                href="https://www.notion.so/Frontend-developer-1257c5ebb36c804f9f48f9ef42e64263"
                target="_blank"
                rel="noopener noreferrer"
              >
                <SiNotion /> Notion
              </a>
            </div>
          </div>
        </div>
      </div>
      <hr className="ProfileHr" />
      <div className="ProfileSkill" id="Skill">
        <Skill />
      </div>
      <hr className="ProfileHr" />
      <div className="ProfileCareer">
        <Career />
      </div>
    </div>
  );
};

export default Profile;
