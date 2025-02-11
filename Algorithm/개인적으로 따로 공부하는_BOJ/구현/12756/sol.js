const fs = require('fs');

const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n').map(line => line.split(' ').map(Number));

const [aAttack, aHealth] = input[0]; 
const [bAttack, bHealth] = input[1]; 

const roundsA = Math.ceil(aHealth / bAttack); 
const roundsB = Math.ceil(bHealth / aAttack); 

if (roundsA < roundsB) {
  console.log("PLAYER B");
} else if (roundsA > roundsB) {
  console.log("PLAYER A");
} else {
  console.log("DRAW");
}
