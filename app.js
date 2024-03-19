const a = 5;
const b = 2;

let myName = "hyunwoo";
//  let은 const와는 다르게 변할 수 있음
// 밑에 예시를 보면 let을 붙이지 않고 myName 변수만으로 수정이 가능함
console.log(a + b);
console.log(a * b);
console.log(a / b);

console.log("hello " + myName);

myName = "koohyunwoo"
console.log("hello " + myName);


// boolean
//  null : 값이 없다. 
const amIFat = null;
console.log(amIFat);

// undefined 
let something;
console.log(something);


// 일주일의 요일을 만들어서 그룹화 시키자
const mon = "mon";
const tue = "tue";
const wed = "wed";
const thu = "thu";
const fri = "fri";
const sat = "sat";
const sun = "sum";

const daysOfWeek = [mon , tue , wed , thu , fri , sat , sun];

const nonsense = [1, 2, "hello", false, null, true, undefined, "hyunwoo"];

console.log(daysOfWeek, nonsence);