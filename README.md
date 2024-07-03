### react 시작

- npm create vite@latest

- npm i

- npm run dev

### 확장프로그램 설치

- ESLint 설치
- .eslintrc.cjs
- "no-unused-vars": "off",
  "react/prop-types" : "off",

### useRef

- useRef
- Reference 객체를 생성
- 컴포넌트 내부의 변수로 활용 가능
- 어떤 경우에도 리렌더링을 유발하지 않음

### useState

- useState
- State를 생성
- 컴포넌트 내부의 변수로 활용 가능
- 값이 변경되면 컴포넌트 리렌더링

### ReactHooks

- ReactHooks
- 클래스 컴포넌트의 기능을 함수 컴포넌트에서도 이용할 수 있도록 도와주는 메서드들

- React.js의 데이터 흐름
- 단방향 데이터 흐름
- ![alt text](image.png)

### React 라이프사이클 ?

- Mount

  - 서버에서 데이터를 불러오는 작업 !

- Update

  - 어떤 값이 변경되었는지 콘솔에 출력

- UnMount

  - 컴포넌트가 사용하던 메모리 정리

### section 7.2

- 사이드이펙트(SideEffect) 란 ?
  - 우리말로 '부작용'이라는 뜻
  - 리액트에서는 "부수적인 효과","파생되는 효과"정도로 해석 가능

### section08

- 프로젝트 소개
- TodoList

- 할 일 추가
- 할 일 계획세우기

### section10

#### 최적화

- 웹 서비스의 성능을 개선하는 모든 행위를 일컫음
- 아주 단순한 것부터 아주 어려운 방법까지 매우 다양함

#### 일반적인 웹 서비스 최적화 방법

- 서버의 응답속도 개선
- 이미지, 폰트, 코드 파일 등의 정적 파일 로딩 개선
- 불필요한 네트워크 요청 줄임

### React App 내부의 최적화 방법

- 컴포넌트 내부의 불 필요한 연산 방지
- 컴포넌트 내부의 불 필요한 함수 재생성 방지
- 컴포넌트의 불 필요한 리렌더링 방지
