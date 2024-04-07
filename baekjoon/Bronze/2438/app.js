const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

answer = []

for(let i =1; i <= input; i++) answer[i-1] = '*'.repeat(i)
console.log(answer.join("\n"))