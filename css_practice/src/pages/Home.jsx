import Category from "../components/Category";
import Header from "../components/Header";
import ImageItem from "../components/ImageItem";
import "../styles/Header.css";
import "../styles/Category.css";
import "../styles/ImageItem.css";

const Home = () => {
  return (
    <div>
      <div>
        <Header title={"홈페이지"} />
      </div>
      <hr />
      <Category />
      <ImageItem />
    </div>
  );
};

export default Home;
