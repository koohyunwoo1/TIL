// 분산적인 조건부 타입

type StringNumberSwitch<T> = T extends number ? string : number;

let a: StringNumberSwitch<number>;
// string
let b: StringNumberSwitch<string>;
// number
let c: StringNumberSwitch<number | string>;
// 조건부 타입에 유니온을 할당해버리면
// 분산적인 조건부로 바뀜

// string | number

// 실용적인 예제

type Exclude<T, U> = T extends U ? never : T;

type A = Exclude<number | string | boolean, string>;

// 1 단계
// Exclude<number, string> |
// Exclude<string, string> |
// Exclude<boolean, string> |

// 2 단계
// number |
// never |
// boolean |

// 결과
// number | boolean

type Extract<T, U> = T extends U ? T : never;

type B = Extract<number | string | boolean, string>;
// 1 단계
// Extract<number, string> |
// Extract<string, string> |
// Extract<boolean, string> |

// 2 단계

// never |
// string |
// never |

// 최종 결과
// string
