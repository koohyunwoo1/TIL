import React from "react";
import "../style/Components/Profile.css";

const Profile = () => {
  return (
    <div className="Profile">
      <div>구현우</div>
      <div>1999.07.07</div>
      <div className="Badges">
        <span className="Badge">Front-end Developer</span>
        <span className="Badge">React.js</span>
      </div>
      <div>안녕하세요. 개발과 지식의 성장을 즐기는 개발자 구현우 입니다</div>
    </div>
  );
};

export default Profile;
