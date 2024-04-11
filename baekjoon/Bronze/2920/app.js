let fs = require('fs');
// let input = fs.readFileSync('input.txt').toString().split(' ');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
// trim : 문자열 앞 뒤에 공백을 제거해준다.
arr = [1,2,3,4,5,6,7,8]

let int_input = input.map(Number);
// 배열 input의 각 요소에 대해 Number 함수를 적용하여 숫자로 변환하는 메서드
reverse_arr = [...arr].sort(function(a, b) { return b - a;});
// arr.sort는 원본 배열을 변경하기 때문에 
// [...arr]을 통해서 복사된 arr을 이용한다.
if (JSON.stringify(int_input) === JSON.stringify(arr)) {
  console.log('ascending')
} else if (JSON.stringify(int_input) === JSON.stringify(reverse_arr)) {
  console.log('descending')
} else {
  console.log('mixed')
}