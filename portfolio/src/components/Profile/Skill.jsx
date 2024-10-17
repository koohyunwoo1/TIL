import React, { useEffect, useRef, useState } from "react";
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
  const skills = [
    {
      title: "Language",
      items: [
        { name: "JavaScript", icon: <FaJs />, percent: 65, className: "js" },
        {
          name: "TypeScript",
          icon: <SiTypescript />,
          percent: 30,
          className: "ts",
        },
        { name: "HTML5", icon: <FaHtml5 />, percent: 70, className: "html" },
        { name: "CSS3", icon: <FaCss3Alt />, percent: 70, className: "css" },
        {
          name: "Python",
          icon: <FaPython />,
          percent: 70,
          className: "python",
        },
      ],
    },
    {
      title: "Framework",
      items: [
        {
          name: "React.js",
          icon: <SiReact />,
          percent: 70,
          className: "react",
        },
        {
          name: "React Native",
          icon: "📱",
          percent: 30,
          className: "react-native",
        },
        {
          name: "Android",
          icon: <SiAndroid />,
          percent: 30,
          className: "android",
        },
        {
          name: "Vue.js",
          icon: <IoLogoVercel />,
          percent: 30,
          className: "vue",
        },
        {
          name: "Django",
          icon: <SiDjango />,
          percent: 20,
          className: "django",
        },
      ],
    },
    {
      title: "Library",
      items: [
        {
          name: "Bootstrap",
          icon: <SiBootstrap />,
          percent: 50,
          className: "bootstrap",
        },
      ],
    },
    {
      title: "Tools",
      items: [
        {
          name: "Visual Studio",
          icon: <SiVisualstudio />,
          percent: 80,
          className: "visualstudio",
        },
        { name: "Figma", icon: <SiFigma />, percent: 70, className: "figma" },
        {
          name: "Notion",
          icon: <SiNotion />,
          percent: 50,
          className: "notion",
        },
        { name: "JIRA", icon: <SiJira />, percent: 70, className: "jira" },
        { name: "MySql", icon: <SiMysql />, percent: 30, className: "mysql" },
        { name: "Git", icon: <SiGit />, percent: 70, className: "git" },
      ],
    },
  ];

  const [isVisible, setIsVisible] = useState(false);
  const skillRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        } else {
          setIsVisible(false);
        }
      },
      { threshold: 0.1 }
    );

    if (skillRef.current) {
      observer.observe(skillRef.current);
    }

    return () => {
      if (skillRef.current) {
        observer.unobserve(skillRef.current);
      }
    };
  }, []);

  return (
    <div ref={skillRef}>
      <div className="Skill">
        <i
          className="fas fa-project-diagram"
          style={{ marginRight: "10px" }}
        ></i>
        Skill
      </div>

      {skills.map((skillGroup, index) => (
        <div className="SkillSection" key={index}>
          <div className="SkillSubTitle">{skillGroup.title}</div>
          <div className="SkillBadges">
            {skillGroup.items.map((skill, idx) => (
              <div className="SkillBadgeContainer" key={idx}>
                <span className={`SkillBadge ${skill.className}`}>
                  {skill.icon} {skill.name}
                </span>
                <div className="SkillProgress">
                  <div
                    className="SkillProgressBar"
                    style={{
                      width: isVisible ? `${skill.percent}%` : "0%",
                      transition: "width 1s ease-in-out",
                    }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default Skill;
