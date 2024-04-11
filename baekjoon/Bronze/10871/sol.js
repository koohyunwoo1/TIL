const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let value = input[0].split(" ");
let N = Number(value[0]);
let X = Number(value[1]);


let A = input[1].split(" ");

for(i = 0; i < N; i++ ) { 
  if (A[i] < X) {
    console.log(A[i])
  }
}