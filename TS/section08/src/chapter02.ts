// keyOf 연산자

interface Person {
  name: string;
  age: number;
}

// type Person2 = {
//   name: string;
//   age: number;
// };

function getPropertyKey(person: Person, key: keyof typeof person) {
  return person[key];
}

const person: Person = {
  name: "구현우",
  age: 27,
};

getPropertyKey(person, "name");
