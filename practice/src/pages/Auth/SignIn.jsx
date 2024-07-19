import React from "react";
import "../../styles/SignIn.css";
import LogOutHeader from "../../components/Home/LogOutHeader";

const SignIn = () => {
  return (
    <div>
      <LogOutHeader />
      <div className="SignIn">
        <h2>로그인 페이지</h2>
      </div>
    </div>
  );
};

export default SignIn;
