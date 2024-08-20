// 기본타입간의 호환성

let num1: number = 10;
let num2: 10 = 10;

num1 = num2;

// 객체 티입간의 호환성
// -> 어떤 객체타입을 다른 객체타입으로 취급해도 괜찮은가 ?

type Animal = {
  name: string;
  color: string;
};

type Dog = {
  // 프로퍼티
  name: string;
  color: string;
  breed: string;
};

let animal: Animal = {
  name: "기린",
  color: "yellow",
};

let dog: Dog = {
  name: "돌돌이",
  color: "brown",
  breed: "진도",
};

animal = dog;
// animal안에 도그를 넣는다

// dog = animal;
// dog안에 animal을 넣는다.

// 슈퍼타입
type Book = {
  name: string;
  price: number;
};

// 서브타입
type ProgrammingBook = {
  name: string;
  price: number;
  skill: string;
};

let book: Book;
let programmingBook: ProgrammingBook = {
  name: "한 입 크기로 잘라먹는 리액트",
  price: 3000,
  skill: "reactjs",
};

book = programmingBook;
// programmingBook = book

// 초과 프로퍼티 검사
// 객체 리터럴 방법을 사용했을시에 발동된다.

// let book2: Book = {
//   name: "한 입 크기로 잘라먹는 리액트",
//   price: 3000,
//   skill: "reactjs",
// };

// 아래 2가지의 방법으로 하자
let book3: Book = programmingBook;

function func(book: Book) {}
func({
  name: "한 입 크기로 잘라먹는 리액트",
  price: 33000,
});

func(programmingBook);
