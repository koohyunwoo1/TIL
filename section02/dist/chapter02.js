// 배열타입을 정의하는 방법
let numArr = [1, 2, 3];
let strArr = ["hello", "im", "winterlood"];
let boolArr = [true, false, true];
// 배열에 들어가는 요소들의 타입이 다양한 경우
let multiArr = [1, "hello"];
// 다차원 배열의 타입을 정의하는 방법
let doubleArr = [
    [1, 2, 3],
    [4, 5],
];
// 튜플(타입스크립트에서만 제공되는 타입)
// 길이와 타입이 고정된 배열
let tup1 = [1, 2];
// tup1 = [1,2,3]
// tup1 = ['hi','hi']
// 위의 두개의 방법으로는 tup1을 다시 지정할수없음
let tup2 = [1, "2", true];
tup1.push(1);
// tup1의 길이를 2개로 지정해놨는데 push를 했는데 오류가 왜 발생안할까 ?
// 배열메서드를 사용할 경우에는 튜플의 길이제한이 발동하지 않는다.
tup1.pop();
tup1.pop();
tup1.pop();
export {};
// 튜플을 사용할때에 유용한 예
// const users: [string, number][] = [
//   ["이정환", 1],
//   ["이정", 2],
//   ["이", 3],
//   ["이정환환", 4],
//   [5, "최아무개"],
// ];
