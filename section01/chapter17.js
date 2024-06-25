// 1. 배열 생성
let areA = new Array(); // 배열 생성자
let areB = []; // 배열 리터럴


let areC = [1,2,3,
  true,
  'hello',
  null,
  undefined,

]


// 2. 배열 요소 접근

let item1 = areC[0];
let item2 = areC[1];

areC[0] = 'hello';
console.log(areC)
console.log(item1, item2)