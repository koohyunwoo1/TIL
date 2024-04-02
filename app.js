const a = 5;
const b = 2;
// const : 기본값으로 작성하자
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

// const mon = "mon";
// const tue = "tue";
// const wed = "wed";
// const thu = "thu";
// const fri = "fri";
// const sat = "sat";
// const sun = "sum";

// const daysOfWeek = [mon , tue , wed , thu , fri , sat , sun];

// const nonsense = [1, 2, "hello", false, null, true, undefined, "hyunwoo"];

// console.log(daysOfWeek, nonsense);


// array

const daysOfWeek = ["mon" , "tue" , "wed" , "thu" , "fri" , "sat" , "sun"];

// Get Item from Array
console.log(daysOfWeek[4])  
// fri

// Add one more day to the array
daysOfWeek.push('hi')  
// hi라는 단어 추가해줌
console.log(daysOfWeek)

// practice

const toBuy = ["potato", "tomato", "pizza"]

toBuy.push("gimbab")
// gimbab이라는 단어 추가해줌
console.log(toBuy)

// 2.6 Objects

const playerName = 'nico';
const playerPoints = 121212;
const playerHandsome = false;
const playerFat = 'little bit';

// 위에서 하는거는 비효율적이다.

const player = {
  name : "nico",
  points : 10,
  fat : true,
};
console.log(player.name);
console.log(player['name']);

// 위의 2개는 같은 의미를 한다.


console.log(player);
player.lastName = "potato";
player.points += 15;
// points가 바뀌는 것을 확인할 수 있음
console.log(player.points);


// 2.7 Functions part One
function sayHello(nameOfPerson, age){
  console.log("Hello my name is " + nameOfPerson + "and I am " + age);
}

sayHello("nico", 10);
sayHello("dal", 23);
sayHello("lynn", 21);


function plus(a, b){
  console.log(a + b);
}

plus(2, 3);

