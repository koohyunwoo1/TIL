// 선언 합침

interface Person {
  name: string;
}

interface Person {
  //   name: number;
  // 동일한 변수를 선언할거면 타입도 같게 해줘야 한다.
  // 서브타입도 안됨
  age: number;
}

// 인터페이스는 동일한 변수로 선언해도 가능하다

const person: Person = {
  name: " ",
  age: 27,
};

// 모듈 보강

interface Lib {
  a: number;
  b: number;
}

interface Lib {
  c: string;
}
const lib = {
  a: 1,
  b: 2,
  c: "hello",
};
