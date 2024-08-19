const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let A = input[0]
let B = input[1]
let C = input[2]

console.log(A)
console.log(B)
console.log(C)

let num = A * B * C
console.log(num)


// 못 풀었음