import Header from "../components/Header";
import Test from "../components/Test";
import Test2 from "../components/Test2";
import Test3 from "../components/Test3";
import Test4 from "../components/Test4";
import "../styles/Home.css";

const Home = () => {
  return (
    <div>
      <div className="container">
        <Header />
        <div className="components-wrapper">
          <h1 className="title">Revolutionize Your Running.</h1>
          <h3 className="subtitle">
            Start your journey to a healthier, stronger you with our running
            website.
          </h3>
          <div className="component-wrapper">
            <div className="component">
              <Test />
            </div>
            <div className="component">
              <Test2 />
            </div>
          </div>
        </div>
      </div>
      <div className="component-test3">
        <Test3 />
      </div>
      <div>
        <Test4 />
      </div>
    </div>
  );
};

export default Home;
