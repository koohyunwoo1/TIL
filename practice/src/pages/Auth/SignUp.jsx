import React, { useState } from "react";
import "../../styles/Auth/SignUp.css";
import LogOutHeader from "../../components/Home/LogOutHeader";

const SignUp = () => {
  return (
    <div>
      <LogOutHeader />
      <div className="SignUp">회원가입</div>
    </div>
  );
};

export default SignUp;
