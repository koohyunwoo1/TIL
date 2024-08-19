import "./Header.css";
import { memo } from "react";

const Header = () => {
  return (
    <div className="Header">
      <h3>오늘은 📆</h3>
      <h1>{new Date().toDateString()}</h1>
    </div>
  );
};

// 인수로 받은 Header를 props가 변경되지 않았을 때에는 리 렌더링 하지 않도록

export default memo(Header);
