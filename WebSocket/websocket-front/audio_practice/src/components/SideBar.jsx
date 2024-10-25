import { Link } from "react-router-dom";
import "../style/SideBar.css";
const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>사이드바</h2>
      <ul>
        <li>
          <Link to="/">홈</Link>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
