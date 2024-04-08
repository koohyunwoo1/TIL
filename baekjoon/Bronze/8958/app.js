const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = parseInt(input[0])

for (let i=1; i< T+1; i++) {
  let cnt = 0;
  let sum = 0;

  for (let j=0; j< input[i].length; j++){
    if (input[i][j] === 'O') {
      cnt ++;
    } else {
      cnt = 0;
    }
    sum += cnt;
  
  }
  console.log(sum)
}




