import React, { useState } from "react";
import "../../style/Profile/Skill.css";
import Modal from "../common/Modal";

const Skill = () => {
  const hardSkills = [
    {
      title: "Language",
      items: [
        {
          name: "JavaScript",
          imageSrc: "/assets/skills/JavaScript.png",
          className: "js",
          description: (
            <>
              - ES6 이후의 문법: 템플릿 리터럴, 화살표 함수, 스프레드 연산자
              등을 활용할 수 있습니다.
              <br />- async/await와 Fetch API를 사용해 비동기 작업 및 서버와의
              동적 통신을 구현했습니다.
            </>
          ),
        },
        {
          name: "TypeScript",
          imageSrc: "/assets/skills/TypeScript.png",
          className: "ts",
          description: (
            <>
              - JavaScript의 타입 안정성을 제공하여 유지보수성과 가독성을 높일
              수 있습니다.
              <br />- React와 같은 라이브러리와 함께 사용해 타입 안정성을
              보장하며 오류를 줄일 수 있습니다.
            </>
          ),
        },
        {
          name: "HTML5",
          imageSrc: "/assets/skills/HTML5.png",
          className: "html",
          description: (
            <>
              - 시맨틱 태그를 활용해 구조적이고 접근성 높은 웹 페이지를 설계할
              수 있습니다.
              <br />- 최신 브라우저 API를 사용해 동적인 웹 기능을 구현할 수
              있습니다.
            </>
          ),
        },
        {
          name: "CSS3",
          imageSrc: "/assets/skills/CSS3.png",
          className: "css",
          description: (
            <>
              - CSS3를 사용해 스타일링과 레이아웃 설계를 할 수 있으며, 반응형
              디자인을 구현할 수 있습니다.
              <br />- Flexbox와 Grid를 활용해 복잡한 레이아웃을 효율적으로
              개발할 수 있습니다.
            </>
          ),
        },
        {
          name: "Python",
          imageSrc: "/assets/skills/Python.png",
          className: "python",
          description: (
            <>
              - Python을 사용해 데이터 분석 및 간단한 스크립트를 작성할 수
              있습니다.
              <br />- Django를 사용해 웹 서버를 구축한 경험이 있습니다.
            </>
          ),
        },
      ],
    },
    {
      title: "Framework",
      items: [
        {
          name: "React.js",
          imageSrc: "/assets/skills/React.png",
          className: "react",
          description: (
            <>
              - React를 사용해 UI를 컴포넌트 기반으로 설계하고, 동적 웹
              애플리케이션을 개발할 수 있습니다.
              <br />- 상태 관리 라이브러리(Redux, Zustand, Context API 등)를
              사용해 대규모 웹 서비스를 관리할 수 있습니다.
            </>
          ),
        },
        {
          name: "ReactNative",
          imageSrc: "/assets/skills/ReactNative.png",
          className: "react-native",
          description: (
            <>
              - React Native로 모바일 애플리케이션을 개발한 경험이 있습니다.
              <br />- 네이티브 모듈 연동과 애니메이션 처리를 통해 사용자 경험을
              향상시켰습니다.
            </>
          ),
        },
        {
          name: "Vue.js",
          imageSrc: "/assets/skills/Vue.png",
          className: "vue",
          description: (
            <>
              - Vue.js로 간단한 SPA(Single Page Application)를 구현한 경험이
              있습니다.
              <br />- Pinia를 활용한 상태 관리와 컴포넌트 기반 설계 경험이
              있습니다.
            </>
          ),
        },
      ],
    },
    {
      title: "Tools",
      items: [
        {
          name: "Figma",
          imageSrc: "/assets/skills/Figma.png",
          className: "figma",
          description: (
            <>
              - UI/UX 디자인 협업 도구로 사용하며, 프로토타입을 설계한 경험이
              있습니다.
              <br />- 컴포넌트 기반 설계와 Auto Layout을 활용해 효율적으로
              디자인을 제작할 수 있습니다.
            </>
          ),
        },
        {
          name: "Notion",
          imageSrc: "/assets/skills/Notion.png",
          className: "notion",
          description: (
            <>
              - 팀 협업 및 프로젝트 관리 도구로 사용하며, 효율적인 작업 흐름을
              구성했습니다.
              <br />- 데이터베이스와 템플릿을 활용해 체계적인 문서화를 진행할 수
              있습니다.
            </>
          ),
        },
        {
          name: "JIRA",
          imageSrc: "/assets/skills/Jira.png",
          className: "jira",
          description: (
            <>
              - 애자일 기반 프로젝트 관리를 위해 사용하며, 스프린트 및 태스크
              관리를 효율적으로 수행했습니다.
              <br />- JIRA 보드를 활용해 팀 내 작업 진행 상황을 시각적으로
              관리했습니다.
            </>
          ),
        },
        {
          name: "Git",
          imageSrc: "/assets/skills/Git.png",
          className: "git",
          description: (
            <>
              - Git을 활용해 버전 관리를 체계적으로 수행하고, 협업 시 브랜치
              전략을 사용합니다.
              <br />- GitHub Actions를 통해 CI/CD 자동화를 경험했습니다.
            </>
          ),
        },
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
              을 가장 중요하게 생각하며,
              <strong
                style={{
                  color: "orange",
                  fontSize: "18px",
                  fontWeight: "bold",
                  fontStyle: "oblique",
                }}
              >
                팀워크
              </strong>
              를 통해 협력하는 것을 선호합니다. 팀원들과의 열린 대화를 통해
              아이디어를 나누고, 명확하게 의견을 전달하는 것이 중요하다고
              믿습니다.
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

  // const [isModalVisible, setModalVisible] = useState(false);
  // const [modalContent, setModalContent] = useState("");

  // const openModal = (description) => {
  //   setModalContent(description);
  //   setModalVisible(true);
  // };

  // const closeModal = () => {
  //   setModalContent("");
  //   setModalVisible(false);
  // };

  return (
    <div>
      <div className="Skill">
        <h2 className="SkillTitle">Hard Skills</h2>
        {hardSkills.map((skillGroup, index) => (
          <div className="SkillSection" key={index}>
            <h3 className="SkillSubTitle">{skillGroup.title}</h3>
            <div className="SkillBadges">
              {skillGroup.items.map((skill, idx) => (
                <div className="SkillBadgeContainer" key={idx}>
                  <img
                    src={skill.imageSrc}
                    alt={skill.name}
                    className="SkillBadgeImage"
                  />
                  <span className="SkillBadgeText">{skill.name}</span>
                  <div className="SkillDescription">{skill.description}</div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="SkillSection">
        <h2 className="SoftSkill">Soft Skills</h2>
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
