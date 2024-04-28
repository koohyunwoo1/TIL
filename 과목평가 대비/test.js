// html을 안건들이고 클래스 : ssafy!를 추가하려면 ?


// span태그를 스스로 만들고, 거기에 클래스 ssafy를 부여한다면 ?


// p태그를 가져 오려면 ?
querySelector('p')

// p태그 안에 div속성 넣기
appendchild

// querySelector로 가져오면 같은 태그여도 제일 위에거를 들고온다.


//1.에러 x 코드?  3

const ssafy = 1
ssafy = 2
//
const ssafy 
//
let ssafy
//
let ssafy = 1
let ssafy = 2

//2.출력 결과? 0 1 2

const numbers = [ 1,2,3 ]
for ( const number in numbers ) {
  console.log(number)
}

//3.출력결과?  0출력되고 에러
for (const i = 0; i < 10; i++ ) {
    console.log(i)
}

//4.출력결과
console.log(x)
var x = 1
// undefined

let x
// 에러

const x
// 에러

let x = 1
x = 2
// 에러

//5.출력결과


console.log(ssafy)
var ssafy = "구현우"

// undefined
//5.




for(let i = 0 ; i < 9; i++){
    // scope 이곳에 해당하는 스코프의 이름은?
}   // 블록 스코프 

//6 변수없음을 의도적으로 표현하는 단어?
// null


//7 코드의 결과

function f1 (x, y) {
    return x + y
}

function f2 (x, y) {
    return x * y
}

const f3 = function (x, y) {
    return x(10, 20) + y(30, 40)
}

console.log(f3(f1, f2))

// 1230







// forEach와 map의 차이점을 작성하시오.


const a = [1,2,3] // 2배 한 결과를 출력하시오
const result = []
console.log(a.forEach(e => result.push(e * 2))) // 반환값이 반드시 없xx
console.log(result)
//forEach 1회용 반복을 할때 유리하다

console.log(a.map(e => e * 2))
// map -> 여러번 반복할때 유리한 부분이 있다


// 두배시킨뒤, 3의 배수만 찾아라
console.log(a.map(e => e * 2).filter(el => el % 3 === 0))


// forEach는 반환값이 없다. map은 반환값이 있다


////2번


// Object 구조 분해 할당을 사용하여 배열 student의 객체에서
// age 값만 뽑아서 개별 변수에 할당하려고 한다.
// ⓐ에 들어갈 코드를 작성하시오. (특수문자에 유의하여 공백없이 작성하시오)

const student= {
    Name: 'Daeyoung Yoon',
    age: 26,
    major: 'Business Administration',
}

const { age } = student // === const age = student.age


//3번

// JavaScript에서 '===' 연산자의 역할이 무엇인가요?

// 값 자료형 데이터타입

1 == '1' // true
1 === '1' // false

// 4번

div.addEventListener('click', console.log('누르지 마세요')) // 1

div.addEventListener('click', function(){console.log('누르지 마세요')}) //2

div.addEventListener('click', ()=>{console.log('누르지 마세요')}) // 3

const func = function(){
    console.log('누르지 마세요')
}
div.addEventListener('click', func) //4


// 함수를 만드는 방법 3가지
// 1.함수 선언문(선언식) function a () {}
// 2.함수 표현식        const b = function () {}
// 3.화살표 함수        const c = () => {}


addEventListener('click', function (){console.log('누르지 마세요')})

// call back 다시 부른다 부른다 다시



// def a():
//   print(100000000000)

//함수는 정의를해도, 호출하지 않으면 의미 xxx
// a()


//1 페이지를 새로고침 하지 않고 페이지 일부를 바꿀 수 있도록
//하는 비동기적인 웹 애플리케이션의 제작을 위한 웹 개발 기법의 이름은?


//2,3


// Promise 객체에 대한 설명으로 옳지 않은 것을 고르시오.
	
// 1 Promise 객체의 .then 메서드를 통해 정상적인 동작이 진행된 경우의 실행할 코드를 작성할 수 있다.
	
// 2 .then에 .catch를 연결해서 바로 사용할 수 있는 이유는 .then의 반환 값이 Promise 객체이기 때문이다.

// 3. Promise 객체를 사용하면 가독성이 떨어지고 유지 보수가 어려워지기 때문에 콜백 함수 형태로 사용하는 것이 바람직하다.

// 4. Promise 객체의 .catch 메서드를 통해 거부된 경우의 실행할 코드를 작성한다.

// 5. Promise 객체는 .then 메서드를 통해 Promise가 이행된 경우의 실행할 함수를 정의한다.

// 6. .then에 .catch를 연결해서 바로 사용할 수 있는 이유는 .then의 반환 값이 Promise 객체이기 때문이다.

// 7. async 함수 내의 모든 Promise 객체는 항상 동기적으로 동작한다.

// 8. Promise 객체는 .catch 메서드를 통해 Promise가 거부된 경우의 실행할 함수를 정의한다.




// 4.

// 변수 a에서 false 항목들만 추리는 코드를 작성하려 한다.
// _에 들어갈 코드를 작성하시오. (대소문자에 유의하여 작성하시오.)

let a= [
  { a: 'h', b: false },
  { a: 'w', b: true },
  { a: 'r', b: false },
]

a= a.filter(function (c) {
  return !c.b 
    //{ a: 'h', b: false }, c -> 객체 c.b -> !false/true
})



// 5 네가지중 종류가 다른 하나는?
object //참조자료형
array //참조자료형
null //원시자료형
function //참조자료형


// 6 Object '속성명 축약'을 사용하여 배열
// a와 b를 가지는 객체 c를 정의하려고 한다.
// _에 들어갈 코드로 옳은 것을 고르시오.

const a = [ 'a1', 'a2', 'a3' ]
const b = [ 'b1', 'b2', 'b3' ]

const c = {
    a : a,
    b : b
}

const c = {
    a,
    b
}


//다음 중 지문의 코드를 실행했을 때, 변수 b의 결과?

// const a = [
//     { a: 10, b: 10 },
//     { a: 20, b: 20 },
//     { a: 30, b: 30 },
// ]
  
// const b= a.map(function (a) {
//     return { c: a.a / a.b }
// })


// 다음 중, callback 함수 O X.

// 다른 함수에 인자로 전달된 함수를 의미한다.
// JavaScript만의 독특한 함수이다. 
// 익명 함수와 기명 함수 둘 다 callback 함수로 사용가능하다.
// 비동기 작업이 완료된 후 코드 실행을 계속하는데 사용되는 경우를 비동기
// callback이라고 한다.


// 다음 중 JavaScript의 function에 대한 설명 OX

// 함수의 정의 방법 중 함수 선언식은 함수의 이름과 함께 정의 하는 방식이다.
// 함수의 정의 방법 중 함수 표현식은 함수의 이름을 반드시 정의하여야 한다.
// 함수를 정의할 때 이름을 생략 할 수 있다.
// JavaScript의 function은 참조 타입에 속한다.


// 다음 중 JSON에 관한 설명 OX

// 1Object 기반의 데이터 포맷이기 때문에, 다른 모든 Object 기반의 언어에서
// 별도의 변환 없이 사용 가능하다.

// 2JSON은 JavaScript Object Notation의 약자이다.

// 3독립된 파일 형태로는 저장 할 수 없다.

// 4오직 JavaScript에서만 사용 가능하며 다른 언어는 JSON 데이터를 사용 할 수 없다.

