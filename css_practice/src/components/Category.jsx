import "../styles/Category.css";
import Button from "../components/Button";

const Category = () => {
  return (
    <div className="Category">
      <div className="left">
        <h1>FitCunnect</h1>
      </div>
      <div className="right">
        <div>
          <Button text={"회원가입"} />
        </div>
        <div>
          <Button text={"캘린더"} />
        </div>
        <div>
          <Button text={"커뮤니티"} />
        </div>
        <div>
          <Button text={"마이페이지"} />
        </div>
      </div>
    </div>
  );
};

export default Category;
