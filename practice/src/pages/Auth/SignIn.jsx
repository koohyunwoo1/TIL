import React from "react";
import "../../styles/SignIn.css";
import LogOutHeader from "../../components/Home/LogOutHeader";
import Login from "../../components/Home/Login";
const SignIn = () => {
  return (
    <div>
      <LogOutHeader />
      <div className="SignIn">
        <Login />
      </div>
    </div>
  );
};

export default SignIn;
