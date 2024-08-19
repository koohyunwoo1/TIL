// 객체 리터럴 타입
let user: {
  id?: number;
  // ? 를 넣었을 경우 있어도 되고 없어도 되는 경우이다.

  name: string;
} = {
  id: 1,
  name: "구현우",
};

user = {
  name: "홍길동",
};

let config: {
  readonly apiKey: string;
  // 절대 값이 바뀌면 안되는 경우가 있다면
  // readonly 설정을 해주면 된다.
} = {
  apiKey: "MY API KEY",
};
