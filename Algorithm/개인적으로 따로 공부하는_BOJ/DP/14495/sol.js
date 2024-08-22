const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
// const input = fs.readFileSync(0, "utf-8").toString().trim();
// const input = fs.readFileSync("14495/input.txt").toString().trim();

const dp = [0, 1, 1, 1];

for (let i = 4; i < 117; i++) {
  dp.push(dp[i - 1] + dp[i - 3]);
}
console.log(parseInt(dp[input]));
