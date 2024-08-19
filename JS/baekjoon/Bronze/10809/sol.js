const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split(' ');
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');

let S = input[0];
let alphabet = 'abcdefghijklmnopqrstuvwxyz';
let result = Array(26);
// 길이가 26인 배열을 생성한다.

for (let i = 0; i < alphabet.length; i++) {
  result[i] = S.indexOf(alphabet[i]);
}
// 알바벳의 첫 등장위치를 알려준다.

console.log(result.join(' '));