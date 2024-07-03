import { useReducer } from "react";

// reducer : 변환기
// -> 상태를 실제로 변환시키는 변환기 역할
function reducer(state, action) {
  switch (action.type) {
    case "INCREASE":
      return state + action.data;
    case "DECREASE":
      return state - action.data;
    default:
      return state;
  }

  // switch 문을 이용해서 action.type이 INCREASE라면
  // + 해주고 다르면 - 해준다.

  //   if (action.type === "INCREASE") {
  //     return state + action.data;
  //   } else if (action.type === "DECREASE") {
  //     return state - action.data;
  //   }
}
// 2. reducer함수 호출

const Exam = () => {
  // dispatch : 발송하다, 급송하다
  // -> 상태 변화가 있어야 한다는 사실을 알리는, 발송하는 함수
  const [state, dispatch] = useReducer(reducer, 0);
  // useReducer , 첫번째 인수에는 상태를 실제로 변환시키는 변환기 역할을 하는 함수를 넣어주면 되고,
  // 두번째 인수에는 state의 초기값을 넣어주면 된다.

  const onClickPlus = () => {
    // 인수 : 상태가 어떻게 변화되길 원하는지 ?
    dispatch({
      type: "INCREASE",
      data: 1,
    });

    // 1. dispatch 호출
  };
  const onClickMinus = () => {
    dispatch({
      type: "DECREASE",
      data: 1,
    });
  };

  return (
    <div>
      <h1>{state}</h1>
      <button onClick={onClickPlus}>+</button>
      <button onClick={onClickMinus}>-</button>
    </div>
  );
};

export default Exam;
