import React, { useState } from "react";
import "../../styles/Header.css";
import logo from "../../assets/Logo.png";

const Header = () => {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setSidebarOpen((prevState) => !prevState);
  };

  return (
    <>
      <div className={`header ${isSidebarOpen ? "transparent" : ""}`}>
        <img src={logo} alt="Logo" className="Header-logo" />
        <button className="menu-button" onClick={toggleSidebar}>
          ≡
        </button>
      </div>

      <div className="divC">
        <div className={`sidebar ${isSidebarOpen ? "open" : ""}`}>
          <button className="close-button" onClick={toggleSidebar}>
            X
          </button>
          <div className="sidebar-content">
            <h1 className="category-item">회원가입</h1>
            <h1 className="category-item">캘린더</h1>
            <h1 className="category-item">커뮤니티</h1>
            <h1 className="category-item">마이페이지</h1>
          </div>
        </div>

        <div
          className={`overlay ${isSidebarOpen ? "visible" : ""}`}
          onClick={toggleSidebar}
        ></div>
      </div>
    </>
  );
};

export default Header;
