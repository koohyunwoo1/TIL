import React from "react";
import "../../style/Profile/Profile.css";
import Skill from "./Skill";
import Carrer from "./Carrer";

const Profile = () => {
  return (
    <div>
      <div className="Profile">
        <div className="ProfileImage" />
        <div className="ProfileDetails">
          <div className="ProfileName">구현우</div>
          <div className="ProfileBirth">1999.07.07</div>
          <div className="Badges">
            <span className="Badge">Frontend Developer</span>
            <span className="Badge">React.js</span>
          </div>
          <div className="ProfileIntro">
            안녕하세요 프론트개발자를 꿈꾸고 있는 학생입니다.
          </div>
        </div>
      </div>
      <hr className="ProfileHr" />
      <div className="ProfileSkill" id="Skill">
        <Skill />
      </div>
      <hr className="ProfileHr" />
      <div className="ProfileCarrer">
        <Carrer />
      </div>
    </div>
  );
};

export default Profile;
