// 1000

// const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().split(' ')
// console.log(typeof input)

// const input = fs.readFileSync('/dev/stdin').toString().split(' ');
// const A = parseInt(input[0])
// const B = parseInt(input[1])

// console.log(A + B)


// 1001

// const fs = require('fs');
// // const input = fs.readFileSync('input.txt').toString().split(' ');
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');

// const A = parseInt(input[0])
// const B = parseInt(input[1])

// console.log(A - B)


// const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().split(' ');
// // const input = fs.readFileSync('/dev/stdin').toString().split(' ');

// const calculator = {
//   minus : function(A, B){
//     return A - B;
//   }
// };

// const minusResult = calculator.minus(input[0], input[1])
// console.log(minusResult)

// 1008


// const fs = require('fs');
// // const input = fs.readFileSync('input.txt').toString().split(' ');
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');


// const calculator = {
//   div : function(A, B){
//     return A / B;
//   }
// };

// const divResult = calculator.div(input[0], input[1])
// console.log(divResult)


// 1330

// const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().split(' ');
// // const input = fs.readFileSync('/dev/stdin').toString().split(' ');
// const A = parseInt(input[0]);
// const B = parseInt(input[1]);

// if (A > B) {
//   console.log('>')
// }
// else if (A < B) {
//   console.log('<')
// }
// else {
//   console.log('==')
// };


// //  함수로 풀어보기
// const calculator = {
//   com : function(A, B){
//     if (A > B) {
//       return '>'
//     }
//     else if (A < B){
//       return '<'
//     }
//     else{
//       return '=='
//     }
//   }
// }

// const comResult = calculator.com(parseInt(input[0]), parseInt(input[1]))
// console.log(comResult)


// 2557

// console.log("Hello World!")

// 2475

// const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().split(' ');
// // const input = fs.readFileSync('/dev/stdin').toString().split(' ');

// const calculator = {
//   sum : function(a, b, c, d, e)
// }

// const sumResult = calculator.sum(parseInt())



// 9498

// const fs = require('fs');
// // const input = fs.readFileSync('input.txt').toString().split(' ');
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');
// const num = parseInt(input[0])

// if (90<= num) {
//   console.log('A')
// }
// else if (80 <= num) {
//   console.log('B')
// }
// else if (70 <= num) {
//   console.log('C')
// }
// else if (60 <= num) {
//   console.log('D')
// }
// else {
//   console.log('F')
// }


// 10950
const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = parseInt(input[0]);

for(let i = 1; i < T+1; i++) {
    const num = input[i].split(' ');
  const firstNum = parseInt(num[0]);
  const secondNum = parseInt(num[1]);
  console.log(firstNum + secondNum);
}


// 10951
