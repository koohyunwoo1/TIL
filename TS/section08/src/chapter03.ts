// 맵드 타입
// interface에서 만들수 없다 type써야 함.
interface User {
  id: number;
  name: string;
  age: number;
}

// 맵드 타입의 문법
type PartialUser = {
  [key in keyof User]?: User[key];
};

// 한명의 유저 정보를 불러오는 기능

function fetchUser(): User {
  return {
    id: 1,
    name: "구현우",
    age: 26,
  };
}

// 한명의 유저 정보를 수정하는 기능
function updateUser(user: PartialUser) {
  // 수정하는 기능
}

updateUser({
  //   id: 1,
  //   name: "구현우",
  age: 25,
});

// 변경되는 값만 넣어서 하고싶다.
