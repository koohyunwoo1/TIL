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
  const hardSkills = [
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

  const softSkills = [
    {
      title: "Communication",
      items: [
        {
          des: (
            <>
              저는
              <strong
                style={{
                  color: "orange",
                  fontSize: "18px",
                  fontWeight: "bold",
                  fontStyle: "oblique",
                }}
              >
                소통
              </strong>
              을 가장 중요하게 생각하며, 팀워크를 통해 협력하는 것을 선호합니다.
              팀원들과의 열린 대화를 통해 아이디어를 나누고, 명확하게 의견을
              전달하는 것이 중요하다고 믿습니다. 저는 팀 내에서 서로의 강점을
              살리고 다양한 의견을 존중하며, 협업을 통해 더 나은 결과물을
              만들어내는 것을 지향합니다.
            </>
          ),
        },
      ],
    },
    {
      title: "Problem-Solving",
      items: [
        {
          des: (
            <>
              저는 문제를 분석하고 해결하는 데 있어
              <strong
                style={{
                  color: "orange",
                  fontSize: "18px",
                  fontWeight: "bold",
                  fontStyle: "oblique",
                }}
              >
                논리적이고 창의적인 접근
              </strong>
              을 중요시합니다. 복잡한 문제를 단계적으로 나누어 해결하고, 다양한
              솔루션을 모색하여 최적의 결과를 도출하는 과정을 즐깁니다. 특히
              프론트엔드 개발에서 발생할 수 있는
              <strong
                style={{
                  color: "orange",
                  fontSize: "18px",
                  fontWeight: "bold",
                  fontStyle: "oblique",
                }}
              >
                UI/UX 문제
              </strong>
              를 빠르게 파악하고 해결하려 노력합니다.
            </>
          ),
        },
      ],
    },
    {
      title: "Adaptability",
      items: [
        {
          des: (
            <>
              저는 빠르게 변화하는 기술 환경에
              <strong
                style={{
                  color: "orange",
                  fontSize: "18px",
                  fontWeight: "bold",
                  fontStyle: "oblique",
                }}
              >
                적응하는 능력
              </strong>
              이 중요하다고 생각합니다. 새로운 기술이나 프레임워크가 등장할 때
              유연하게 학습하고, 필요할 경우 기존의 방식을 바꾸는 데 두려움이
              없습니다. 프론트엔드 개발에서 최신 트렌드와 도구들을 적극적으로
              활용하려고 합니다.
            </>
          ),
        },
      ],
    },
    {
      title: "Attention to Detail",
      items: [
        {
          des: (
            <>
              <strong
                style={{
                  color: "orange",
                  fontSize: "18px",
                  fontWeight: "bold",
                  fontStyle: "oblique",
                }}
              >
                작은 디테일
              </strong>
              에도 신경 쓰는 것이 프론트엔드 개발의 핵심이라고 생각합니다.
              사용자 경험을 개선하기 위해 인터페이스의 작은 요소까지 꼼꼼히
              점검하며, 퍼포먼스 최적화와 디자인 일관성에 특별히 주의를
              기울입니다.
            </>
          ),
        },
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
      { threshold: 0.4 }
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

      <div>
        <h2 className="SkillTitle">Hard Skills</h2>
        {hardSkills.map((skillGroup, index) => (
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

      <div className="SkillSection">
        <h2 className="SkillTitle">Soft Skills</h2>
        <ul className="SoftSkillTitle">
          {softSkills.map((skillGroup, index) => (
            <li key={index} className="SoftSkillText">
              {skillGroup.title}
              <ul className="SoftSkillSubText">
                {skillGroup.items.map((skill, idx) => (
                  <li key={idx}>{skill.des}</li>
                ))}
              </ul>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Skill;
