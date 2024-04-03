

// const a = 5;
// const b = 2;
// // const : 기본값으로 작성하자
// let myName = "hyunwoo";
// //  let은 const와는 다르게 변할 수 있음
// // 밑에 예시를 보면 let을 붙이지 않고 myName 변수만으로 수정이 가능함
// console.log(a + b);
// console.log(a * b);
// console.log(a / b);

// console.log("hello " + myName);

// myName = "koohyunwoo"
// console.log("hello " + myName);


// // boolean
// //  null : 값이 없다. 
// const amIFat = null;
// console.log(amIFat);

// // undefined 
// let something;
// console.log(something);


// // 일주일의 요일을 만들어서 그룹화 시키자

// // const mon = "mon";
// // const tue = "tue";
// // const wed = "wed";
// // const thu = "thu";
// // const fri = "fri";
// // const sat = "sat";
// // const sun = "sum";

// // const daysOfWeek = [mon , tue , wed , thu , fri , sat , sun];

// // const nonsense = [1, 2, "hello", false, null, true, undefined, "hyunwoo"];

// // console.log(daysOfWeek, nonsense);


// // array

// const daysOfWeek = ["mon" , "tue" , "wed" , "thu" , "fri" , "sat" , "sun"];

// // Get Item from Array
// console.log(daysOfWeek[4])  
// // fri

// // Add one more day to the array
// daysOfWeek.push('hi')  
// // hi라는 단어 추가해줌
// console.log(daysOfWeek)

// // practice

// const toBuy = ["potato", "tomato", "pizza"]

// toBuy.push("gimbab")
// // gimbab이라는 단어 추가해줌
// console.log(toBuy)

// // 2.6 Objects

// const playerName = 'nico';
// const playerPoints = 121212;
// const playerHandsome = false;
// const playerFat = 'little bit';

// // 위에서 하는거는 비효율적이다.

// const player = {
//   name : "nico",
//   points : 10,
//   fat : true,
// };
// console.log(player.name);
// console.log(player['name']);

// // 위의 2개는 같은 의미를 한다.


// console.log(player);
// player.lastName = "potato";
// player.points += 15;
// // points가 바뀌는 것을 확인할 수 있음
// console.log(player.points);

// // 2.7~ Functions part

// function sayHello(nameOfPerson, age){
//   console.log("Hello my name is " + nameOfPerson + "and I'm " + age);
// }

// sayHello("nico", 10);
// sayHello("dal", 23);
// sayHello("lynn", 21);


// // function plus(a, b){
// //   console.log(a + b);
// // }

// // plus(2, 3);

// // function divide(a, b){
// //   console.log(a / b);
// // }

// // divide(98, 20)

// // player object



// const player = {
//   name : "nico",
//   sayHello : function (otherPersonsName) {
//     console.log("hello ! " + otherPersonsName + " nice to meet you !");
//   },
// };


// console.log(player.name);


// player.sayHello("lynn");


// 2. 9 Recap

// const와 let의 차이는 let은 업데이트를 할 수 있다는 점이다.

// NULL -> 비어있음
// undefined -> 비어있음이 존재함
// push -> array의 제일끝에 값이 들어간다.



// 2. 10 Recap2

// const player =  {
//   name : 'hyunwoo',
//   age : 98,
// };


// console.log(player);
// player.name = "nico";
// console.log(player);
// player.sexy = "soon";
// console.log(player);

// function plus(a, b) {
//   console.log(a * b);
// };

// plus(2, 5, 6, 6, 6, 6, 6, 3, 3);
// 아무리 많은 값을 적어도 
// 제일 처음 나온 2개의 값 a, b 만 선정해서 함수를 실행한다.

// alter : 경고메세지를 띄워주는 것


// 사칙연산 함수 만들어보기

// const calculator = {
//   add : function(a, b){
//     console.log(a + b);
//   },
//   minus : function(a, b){
//     console.log(a - b);
//   },
//   div : function(a, b){
//     console.log(a / b);
//   },
//   multi : function(a, b){
//     console.log(a * b);
//   },
//   power : function(a, b){
//     console.log(a ** b);
//   },
// };


// calculator.add(1, 2)
// calculator.minus(1, 2)
// calculator.div(1, 2)
// calculator.multi(1, 2)
// calculator.power(1, 2)



// 2. 11 Returns
// const age = 96;

// function calculatorKrAge(ageOfForeigner){
//   return ageOfForeigner + 2;
// };

// const krAge = calculatorKrAge(age)

// console.log(krAge);



// // 사칙연산 함수를 return을 이용해서 만들어보기
// const calculator = {
//   add : function(a, b){
//     return a + b;
//   },
//   minus : function(a, b){
//     return a - b;
//   },
//   div : function(a, b){
//     return a / b;
//   },
//   multi : function(a, b){
//     return a * b;
//   },
//   power : function(a, b){
//     return a ** b;
//   },
// };


// const addResult = calculator.add(2, 3);
// const minusResult = calculator.minus(addResult, 3);
// const divResult = calculator.div(2, 3);
// const multiResult = calculator.multi(2, addResult);
// const powerResult = calculator.power(2, 3);
// console.log(addResult)
// console.log(minusResult)
// console.log(divResult)
// console.log(multiResult)
// console.log(powerResult)


// 2.13 Conditionals


// age calculator

// const age = prompt("How old are you ? ");
// prompt -> 경고창 띄우면서 안에 들어있는 인자를 보여준다.


// console.log(typeof age, typeof parseInt(age));
// console.log(age, parseInt(age));

// type을 보는 법 : typeof ~~~
// ~~~의 타입을 보여준다.


// 숫자가 아닌것을 입력했을때 NaN으로 값을 출력해준다.
// parseInt() -> str을 int로 바꿔주는 함수

// const age = parseInt(prompt("How old are you ?"))

// console.log(age)

15

// 2.14 Conditionals2


// console.log(isNaN(age))
// isNaN -> boolean을 반환
// 숫자이면 false를 반환 아니면 ture를 반환

// const age = parseInt(prompt("How old are you ?"));

// if (isNaN(age) || age < 0) {
//   // isNaN : 숫자가 아니면
//   console.log("Please write a real positive number");
// } 
// else if (age < 18 ) {
//   console.log("You are too young.");
// } 
// else if (age >= 18 && age <= 50){
//   // %% == AND , || == OR
//   console.log("You can drink");
// }
// else if (age > 50 && age <= 80){
//   console.log("You should exercise.");
// }
// else {
//   console.log("You can't drink");
// }

const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf8').toString().split(' ');

const A = parseInt(inputdata[0])
const B = parseInt(inputdata[1])

console.log(A + B)
