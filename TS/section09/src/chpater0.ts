// 조건부 타입
// 조건에 따라 타입을 결정

type A = number extends string ? string : number;
// 참이라면 A는 string이 되고
// 거짓이라면 A는 number가 된다.

type ObjA = {
  a: number;
};

type ObjB = {
  a: number;
  b: number;
};

type B = ObjB extends ObjA ? number : string;

// 제네릭과 조건부 타입

type StringNumberSwitch<T> = T extends number ? string : number;
// T가 number 타입으로 확장한다면 string 타입으로
// 그렇지 않다면 number타입으로

let varA: StringNumberSwitch<number>;

let varB: StringNumberSwitch<string>;

function removeSpaces<T>(text: T): T extends string ? string : undefined;
function removeSpaces(text: any) {
  if (typeof text === "string") {
    return text.replaceAll(" ", "");
  } else {
    return undefined;
  }
  // 첫번째 인수들의 해당하는 모든 문자를 찾아서
  // 두번째 인수로 바꿔라
}

let result = removeSpaces("hi im winterlood");
result.toUpperCase();

let result2 = removeSpaces(undefined);
