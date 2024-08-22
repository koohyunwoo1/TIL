// keyOf 연산자
// type Person2 = {
//   name: string;
//   age: number;
// };
function getPropertyKey(person, key) {
    return person[key];
}
const person = {
    name: "구현우",
    age: 27,
};
getPropertyKey(person, "name");
console.log(person);
export {};
