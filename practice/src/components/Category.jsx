import "../styles/Category.css";
import logo from "../assets/logo.png";

const Category = () => {
  return (
    <>
      <div className="header">
        <img src={logo} alt="Logo" className="logo" />
        <div className="title-container">
          <h1 className="category-item">회원가입</h1>
          <h1 className="category-item">캘린더</h1>
          <h1 className="category-item">커뮤니티</h1>
          <h1 className="category-item">마이페이지</h1>
        </div>
      </div>
    </>
  );
};

export default Category;
