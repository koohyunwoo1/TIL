import React from "react";
import "../../style/Profile/Skill.css";
import { FaJs, FaPython, FaHtml5, FaCss3Alt } from "react-icons/fa";
import {
  SiTypescript,
  SiReact,
  SiAndroid,
  SiDjango,
  SiBootstrap,
  SiVisualstudio,
  SiFigma,
  SiNotion,
  SiJira,
  SiMysql,
  SiGit,
} from "react-icons/si";
import { IoLogoVercel } from "react-icons/io5";

const Skill = () => {
  return (
    <>
      <div className="Skill">
        <i
          className="fas fa-project-diagram"
          style={{ marginRight: "10px" }}
        ></i>
        Skill
      </div>

      <div className="SkillSection">
        <div className="SkillSubTitle">Language</div>
        <span className="SkillBadge js">
          <FaJs /> JavaScript
        </span>
        <span className="SkillBadge ts">
          <SiTypescript /> TypeScript
        </span>
        <span className="SkillBadge html">
          <FaHtml5 /> HTML5
        </span>
        <span className="SkillBadge css">
          <FaCss3Alt /> CSS3
        </span>
        <span className="SkillBadge python">
          <FaPython /> Python
        </span>
      </div>

      <div className="SkillSection">
        <div className="SkillSubTitle">Framework</div>
        <span className="SkillBadge react">
          <SiReact /> React.js
        </span>
        <span className="SkillBadge react-native">📱 React Native</span>
        <span className="SkillBadge android">
          <SiAndroid /> Android
        </span>
        <span className="SkillBadge vue">
          <IoLogoVercel /> Vue.js
        </span>
        <span className="SkillBadge django">
          <SiDjango /> Django
        </span>
      </div>

      <div className="SkillSection">
        <div className="SkillSubTitle">Library</div>
        <span className="SkillBadge bootstrap">
          <SiBootstrap /> BootStrap
        </span>
      </div>

      <div className="SkillSection">
        <div className="SkillSubTitle">Tools</div>
        <span className="SkillBadge visualstudio">
          <SiVisualstudio /> Visual Studio
        </span>
        <span className="SkillBadge figma">
          <SiFigma /> Figma
        </span>
        <span className="SkillBadge notion">
          <SiNotion /> Notion
        </span>
        <span className="SkillBadge jira">
          <SiJira /> JIRA
        </span>
        <span className="SkillBadge mysql">
          <SiMysql /> MySql
        </span>
        <span className="SkillBadge git">
          <SiGit /> Git
        </span>
      </div>
    </>
  );
};

export default Skill;
