// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let input = Number(require('fs').readFileSync('/dev/stdin').toString());

let answer = '';

for (let i = input; i >= 1; i--) {
    answer += i + "\n";
}

console.log(answer);