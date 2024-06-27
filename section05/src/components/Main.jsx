import "./Main.css"
// JSX 주의 사항
// 1. 중괄호 내부에는 자바스크립트 표현식만 넣을 수 있다.
// if문이나 for문은 사용 불가
// 2. 숫자 , 문자열, 배열 값만 렌더링 된다.
// true / boolern 값은 렌더링 되지 않는다.
// 3. 모든 태그는 닫혀 있어야 한다.
// 4. 최상위 태그는 반드시 하나어야 한다.


const Main = () => {
  const user = {
    name : '구현우',
    isLogin : true,
  };

  if(user.isLogin) {
    return (
      <div className="logout">
        로그아웃
      </div>
    )
  } else {
    return <div>로그인</div>
  }
  
  // return (
  //   <>
  //     {user.isLogin ? (
  //       <div>로그아웃</div>
  //     ) : (
  //       <div>로그인</div>
  //     )
  //   }
  //   </>
  // )
}

export default Main