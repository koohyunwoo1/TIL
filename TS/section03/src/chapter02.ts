// Unknown 타입

function unknownExam() {
  let a: unknown = 1;
  let b: unknown = "hello";
  let c: unknown = true;
  let d: unknown = null;
  let e: unknown = undefined;

  let unkownVar: unknown;

  //   let num: number = unkownVar;
  //   let str: string = unkownVar;
  //   let bool: boolean = unkownVar;
}

// Never 타입

function neverExam() {
  function neverFunc(): never {
    while (true) {}
  }

  let num: number = neverFunc();
  let str: string = neverFunc();
  let bool: boolean = neverFunc();
}

// Void 타입

function voidExam() {
  function voidFunc(): void {
    console.log("hi");
  }

  let voidVar: void = undefined;
}

// any 타입
// 언노운 타입이 다운캐스팅 되고있는데 any 타입은
// 계층도를 무시하기 때문에 오류가 나지 않는다.
// 웬만하면 사용 하지 말자

function anyExam() {
  let unknownVar: unknown;
  let anyVar: any;
  let undefinedVar: undefined;
  let neverVar: never;
  anyVar = unknownVar;
  undefinedVar = anyVar;

  //   neverVar = anyVar;
  // never 타입은 any타입조차도 무시하지 못한다.
}
