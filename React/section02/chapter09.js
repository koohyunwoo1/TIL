// 5가지 배열 변형 메서드
// 1. filter
// 기존 배열에서 조건에 맞는 요소들만 필터링하여 새로운 배열로 변환

let arr1 = [
  { name : '구현우' , hobby : '테니스'},
  { name : '이정환' , hobby : '테니스'},
  { name : '홍길동' , hobby : '독서'}
]


const tennisPeople = arr1.filter(
  (item) => item.hobby === '테니스'
)

console.log(tennisPeople)


// 2. map
// 배열의 모든 요소를 순회하면서, 각각 콜백함수를 실행하고 그 결과값들을 모아서 새로운 배열을 반환

let arr2 = [1,2,3]

const mapResult1 = arr2.map((item, idx, arr) => {
  return item * 2
})


let names = arr1.map((item) => item.name);
console.log(names)


// 3. sort
// 배열을 사전순으로 정렬
// 문자는 사전순으로 배열이 되지만
// 숫자는 콜백함수를 통해서 조건문을 달아줘야지만 반환이 가능하다.
let arr3 = [10, 3, 5]

arr3.sort((a, b) => {
  if (a > b) {
    // b가 a 앞으로 와라
    return 1;
  }
  else if (a < b) {
    return -1
  }
  else {
    return 0
  }
})

console.log(arr3)


// 4. toSorted
// 정렬된 새로운 배열을 반환하는 메서드

let arr5 = ['c', 'b', 'a'];

const sorted = arr5.toSorted();
console.log(sorted)

// 5. join
// 배열의 모든 요소를 하나의 문자열로 합쳐서 변환하는 그런 메서드

let arr6 = ['hi', 'im', 'winterload']

const joined = arr6.join(' ');

console.log(joined)