const fs = require("fs");
// const input = fs.readFileSync("input.txt").toString().trim();
const input = fs.readFileSync("/dev/stdin").toString().trim();

const dp = [0, 1];

for (i = 2; i < 1000001; i++) {
  dp.push((dp[i - 1] + dp[i - 2]) % 1000000007);
}

console.log(dp[input]);
