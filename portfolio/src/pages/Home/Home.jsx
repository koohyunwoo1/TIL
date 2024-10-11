import React from "react";
import "../../style/Home/Home.css";
import Header from "../../components/Header";
import Name from "../../components/Name";
import Profile from "../../components/Profile";
const Home = () => {
  return (
    <>
      <div className="Container">
        <div className="HeaderContainer">
          <Header />
        </div>
        <div className="NameContainer">
          <Name />
        </div>
        <div>
          <Profile />
        </div>
      </div>
    </>
  );
};

export default Home;
