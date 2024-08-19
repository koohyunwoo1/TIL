// any
// 특정 변수의 타입을 우리가 확실히 모를때
// any타입은 가능한 쓸 일이 없다
let anyVar: any = 10;
anyVar = "hello";

anyVar = true;
anyVar = {};
anyVar = () => {};

anyVar.toUpperCase();
anyVar.toFixed();

let num: number = 10;
num = anyVar;

// unknown

let unknownVar: unknown;

unknownVar = "";
unknownVar = 1;
unknownVar = () => {};
