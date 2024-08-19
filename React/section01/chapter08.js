// 1. null 병합 연산자
// -> 존재하는 값을 추려내는 기능
// -> null, undefined가 아닌 값을 찾아내는 연산자

let var1;
let var2 = 10;
let var3 = 20;

let var4 = var1 ?? var2;
let var5 = var1 ?? var3;
let var6 = var2 ?? var3;
// 처음값인 var2가 나온다.

let useName = '구현우';
let userNickNmae = 'hyunwoo'

let displayName = useName ?? userNickNmae
console.log(displayName)


// 2. typeof 연산자
// -> 값의 타입을 문자별로 변환하는 기능을 하는 연산자

let var7 = 1;
var7 = 'hello';
var7 = true;

let t1 = typeof var7;
console.log(t1)

// 3 삼항 연산자
// -> 합을 3개 사용하는 연산자
// -> 조건사용 이용해서 참, 거짓말 때의 값을 다르게 변환
let var8 = 10;

// 요구사항 : 변수 res에 var8의 값이 짝수 -> "짝", 홀수 -> "홀"

let res = var8 % 2 === 0 ? "짝수" : "홀수";
console.log(res);