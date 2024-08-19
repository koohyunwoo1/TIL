const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let max = Number(input[0])
let max_idx = 0

for (let i = 1; i < 9; i++) { 
  if (max < Number(input[i]) ) {
    max = Number(input[i]);
    max_idx = i;
  }
}

console.log(max)
console.log(max_idx + 1)