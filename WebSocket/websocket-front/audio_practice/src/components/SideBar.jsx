import { Link } from "react-router-dom";
import "../style/SideBar.css";
const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="sidebarTitle">
        음악의 <br />
        재구SoNG
      </div>
      <ul>
        <li>
          <Link to="/">홈</Link>
        </li>
        <li>
          <Link to="/Game">게임</Link>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
