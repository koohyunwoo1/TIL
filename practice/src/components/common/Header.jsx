import "../../styles/Header.css";
import { Link } from "react-router-dom";
import logo from "../../assets/Logo.png";
import { useState } from "react";

const Header = ({ onLogout }) => {
  const [ dropdownOpen, setDropdownOpen ] = useState(false)

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen)
  }
  return (
    <header>
      <nav>
        <div className="navbar">
          <div className="nav-left">
            <img 
              onClick={<Link to="/home" />} 
              src={logo}
              className="logo" 
            />
          </div>
          <div className="nav-right">
            <button 
              className="nav-button"
             onClick={toggleDropdown}
             >
              ≡
            </button>
            {dropdownOpen && (
              <ul className="dropdown">
                <li><Link to="/mypage">마이페이지</Link></li>
                <li><Link to="/report">리포트</Link></li>
                <li><Link to="/community">커뮤니티</Link></li>
                <li><Link to="/" onClick={onLogout}>로그아웃</Link></li>
              </ul>
            )}
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;