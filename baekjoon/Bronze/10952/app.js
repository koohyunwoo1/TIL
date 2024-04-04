const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let ans = ''

for (i=0; i < input.length-1; i++) {
  const num = input[i].split(' ');
  ans += parseInt(num[0]) + parseInt(num[1]) + '\n';
}

console.log(ans)
