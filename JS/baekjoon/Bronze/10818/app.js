const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(input[0])

// console.log(N)

const nums = input[1].split(' ').map(x=> parseInt(x));

// console.log(nums)

let max = nums[0]
let min = nums[0]

for (let i = 0; i < N; i++) {
  if (max < nums[i]) {
    max = nums[i]
  }

  if (min > nums[i]) {
    min = nums[i]
  }
}


console.log(min,max)
