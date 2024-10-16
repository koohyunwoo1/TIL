import React from "react";

// type GreetingProps = {
//   name: string;
//   age: number;
//     isStudent: boolean;
// };

interface GreetingProps {
  name: string;
  age: number;
  //   isStudent: boolean;
}
interface GreetingProps {
  isStudent: boolean;
}

// 2개의 차이가 무엇인가 ?

const Greeting = ({ name, age, isStudent }: GreetingProps) => {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>Age: {age}</p>
      <p>Status: {isStudent ? "학생" : "학생 아님"}</p>
    </div>
  );
};

export default Greeting;
