import React, { useState, useEffect } from "react";
import "../../style/Home/Home.css";
import Header from "../../components/Home/Header";
import HeaderBar from "../../components/Home/HeaderBar";
import Name from "../../components/Profile/Name";
import Profile from "../../components/Profile/Profile";

const Home = () => {
  const [showHeaderBar, setShowHeaderBar] = useState(false);

  const handleArrowClick = () => {
    const profileElement = document.getElementById("profile-section");
    if (profileElement) {
      profileElement.scrollIntoView({ behavior: "smooth" });
    }
  };

  const handleScroll = () => {
    const profileElement = document.getElementById("Skill");
    if (profileElement) {
      const rect = profileElement.getBoundingClientRect();
      if (rect.top <= window.innerHeight && rect.bottom >= 0) {
        setShowHeaderBar(true);
      } else {
        setShowHeaderBar(false);
      }
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <>
      <div className="Container">
        <div className="HeaderContainer">
          <Header />
        </div>
        <div className="NameContainer">
          <Name />
          <div className="arrow" onClick={handleArrowClick}>
            <span></span>
            <span></span>
          </div>
        </div>
        {showHeaderBar && (
          <div
            style={{
              position: "fixed",
              top: 0,
              left: 0,
              right: 0,
              zIndex: 1000,
              width: "80%",
              margin: "0 auto",
              transition: "opacity 0.3s ease",
              opacity: showHeaderBar ? 1 : 0,
            }}
          >
            <HeaderBar />
          </div>
        )}
        <div id="profile-section" className="ProfileContainer">
          <Profile />
        </div>
      </div>
    </>
  );
};

export default Home;
