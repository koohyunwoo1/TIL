import React from "react";
import { Link } from "react-router-dom";
import "../../style/Components/HeaderBar.css";

const HeaderBar = () => {
  return (
    <div className="HeaderBar">
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/project">Projects</Link>
        </li>
      </ul>
    </div>
  );
};

export default HeaderBar;
