// 타입 별칭

type User = {
  id: number;
  name: string;
  nickname: string;
  birth: string;
  bio: string;
  location: string;
};
// User로 지정만 해주면 밑에서 User만 쓰기만 하면 된다.

let user: User = {
  id: 1,
  name: "구현우",
  nickname: "koo",
  birth: "1999.07.07",
  bio: "안녕하세요",
  location: "부산광역시",
};

let user2: User = {
  id: 2,
  name: "홍길동",
  nickname: "koo",
  birth: "1999.07.07",
  bio: "안녕하세요",
  location: "부산광역시",
};

// 인덱스 시그니처

type CountryCodes = {
  [key: string]: string;
};

let contryCodes: CountryCodes = {
  Korea: "ko",
  UnitedState: "us",
  UnitedKingdom: "uk",
};

type CountryNumberCodes = {
  [key: string]: number;
  Korea: number;
};

// let countryNumberAndStringCodes: CountryNumberCodes = {
//   //   Korea: "ko",
// };
