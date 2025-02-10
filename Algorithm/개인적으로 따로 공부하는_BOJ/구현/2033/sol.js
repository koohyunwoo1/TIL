const fs = require('fs');

const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const N = parseInt(fs.readFileSync(filePath).toString().trim());

let digit = 10;
let num = N;

while (num >= digit) {
  num = Math.round(num / digit) * digit; 
  digit *= 10;
}

console.log(num);
