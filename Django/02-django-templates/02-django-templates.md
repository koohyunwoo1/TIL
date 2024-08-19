# Django

## DTL
- Template에서 조건, 반복 변수 등의 프로그래밍적 기능을 제공하는 시스템

### Variable
- render 함수의 세번째 인자로 딕셔너리 데이터를 사용
- 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
- dot('.')를 사용하여 변수 속성에 접근할 수 있음

### Filters
- 표시할 변수를 수정할 때 사용(변수 + '|' + 필터)
- chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
- 약 60개의 built-in templated filters를 제공

### tags
- 반복 or 논리를 수행하여 제어 흐름을 만듦
- 일부 태그는 시작과 종료 태그가 필요
- 약 24개의 built-in template tags를 제공



## 템플릿 상속
1. 페이지의 공통요소를 포함하고
2. 하위 템플릿이 재정의 할 수 있는  공간

- extends tag
- 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림

- bolck tag
- 하위 템플릿에서 제정의 할 수 있는 블록을 정의


## HTML form(요청과 응답)
- 로그인창의 경우는 대부분 form태그이다
- 사용자로부터 할당된 데이터를 서버로 전송
- acting & method
- 데이터를 어디(action)로 어떤 방식(method)으로 보낼지