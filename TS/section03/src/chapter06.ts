// 타입 단언

type Person = {
  name: string;
  age: number;
};

let person = {} as Person;
person.name = "이정원";
person.age = 24;

type Dog = {
  name: string;
  color: string;
};

let dog = {
  name: "돌돌이",
  color: "brown",
  bread: "진도",
} as Dog;

// 타입 단언의 규칙
// 값 as 단언 < - 단언식
// A as B
// A가 B의 슈퍼타입이거나
// A가 B의 서브타입이어야 함

let num1 = 10 as never;
let num2 = 10 as unknown;

// let num3 = 10 as string;
// num3 같은 경우는 겹치지 않기 때문에 오류가 발생함
let num4 = 10 as unknown as string;
// 살짝 편법 ?

// const 단언

let num5 = 10 as const;
// const로 선언한것과 동일한 효과

let cat = {
  name: "야옹이",
  color: "yellow",
} as const;

// Non Null 단언

type Post = {
  title: string;
  author?: string;
  // 익명으로 쓸수도 있기에 선택적 프로퍼티로 설정
};

let post: Post = {
  title: "게시글1",
  author: "이정원",
};

const len: number = post.author!.length;
// ? : author 값이 없으면 전체를 null이나 undefined로 설정
// ! : author 값이 null이나 undfined가 아닐거라고 선언
