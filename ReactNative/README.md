# React Native

### 프로젝트 생성

- npx react-native@0.72.6 init 프로젝트 명 --version 0.72.6

### 프로젝트 생성 후 시작

- 안드로이드 스튜디오에서 개발 환경 시작 한 후 npm start

### 리액트 네이비트 유용한 라이브러리

- 리액트 네이티브에서 모달을 쓸 때 용이한 라이브러리
- react-native-modal, react-native-simple-dialogs

### 초기 설정

- MainActivity.java에 이거 설정

```
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(null);
  }

```

- index.js

```
import 'react-native-gesture-handler';
```

- .eslintrc.js

```
  endOfLine: 'auto', // 이 부분 추가

```

이거 추가

### 모듈 설치

- npm install react-native-gesture-handler

### 프로젝트 생성 한 후에 다른 프로젝트 생성했을시 캐시 지우고 시작하는 방법

- npm start -- --reset-cache
