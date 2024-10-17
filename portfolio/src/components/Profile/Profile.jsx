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
          <div className="ProfileBirth">
            <FontAwesomeIcon icon={faEnvelope} /> kjklovekhw@gmail.com
          </div>
          <div className="Badges">
            <span className="Badge">
              <FontAwesomeIcon icon={faCodeBranch} /> Frontend Developer
            </span>
            <span className="Badge">React.js</span>
          </div>
          <div className="ProfileIntro">
            안녕하세요 프론트개발자를 꿈꾸고 있는 학생입니다.
          </div>
          <div className="ProfileGithub">
            <a
              href="https://github.com/koohyunwoo1"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FontAwesomeIcon icon={faGithub} /> GitHub
            </a>
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
