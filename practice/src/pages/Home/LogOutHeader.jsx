import React from "react";
import { Link } from "react-router-dom";
import logo from "../../assets/Logo.png";
import "../../styles/LogOutHeader.css";

const LogOutHeader = () => {
  return (
    <div className="header-container">
      <div className="header">
        <img src={logo} alt="logo" className="logo" />
        <div className="auth-links">
          <Link to="/signin">
            <h3>로그인</h3>
          </Link>
          <Link to="/signup">
            <h3>회원가입</h3>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default LogOutHeader;
