const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().trim().split(' ');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
// trim : 앞 뒤 공백을 없애준다.

if (input[0] === "" ) {
  console.log(0)
}
else {
  console.log(input.length)
}
