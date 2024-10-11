import React from "react";
import { NavLink } from "react-router-dom";
import "../../style/Components/HeaderBar.css";

const HeaderBar = () => {
  return (
    <div className="HeaderBar">
      <ul>
        <li>
          <NavLink to="/" activeClassName="active">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/project" activeClassName="active">
            Projects
          </NavLink>
        </li>
      </ul>
    </div>
  );
};

export default HeaderBar;
